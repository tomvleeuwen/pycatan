#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  game.py
#  
#  Copyright 2016 Tom van Leeuwen <tom@smokie>
#  

import time
import hashlib
import threading
import struct
from datetime import datetime

import threading

from server import MakeHandlerClass, ThreadedHTTPServer
from board import Board
from btle import BTLE
import config

class KolonistenVanFS(object):
    
    # Game states:
    STATE_INIT          = 0 # Nothing has been done yet.
    STATE_PLAYING       = 2 # Tiles are placed.
    
    def __init__(self, httpcmdobject, btlecmdobject):
        self.httpcmdobject = httpcmdobject
        self.btlecmdobject = btlecmdobject
        self.stats = [0 for _ in xrange(11)]
        self.board = None
        self.game_state = self.STATE_INIT
    
    def get_random_int(self, low, high):
        """ Returns a 'random' integer between low and high-1 """
        rand_number = int(time.time() * 1e6)
        modulo = high - low
        if config.settings['hash_rnd']:
            m = hashlib.sha256()
            m.update(struct.pack("<Q", rand_number))
            hash_str = m.digest()
            rand_number = struct.unpack("<Q", hash_str[-8:])[0]
        return (rand_number % modulo) + low
    
    
    def gpio_down(self):
        """ Start rolling the dice and play a sound, but only when we are playing """
        if self.game_state == self.STATE_PLAYING:
            mp3idx = self.get_random_int(0, len(config.playlist))
            self.append_httpcmd("PLAY_SOUND", config.playlist[mp3idx])
            self.append_httpcmd("DICE_ROLL")
            msg  = str(datetime.now())
            msg += ": Button pressed!"
            self.log(msg)
        
    def gpio_up(self):
        """ Execute the actions for the current state, and go to the next """
        if self.game_state == self.STATE_INIT:
            self.board = Board()
            msg = "Generated board. Place tiles according to the colors of the LEDs."
            self.append_httpcmd("MSG_WRITE", msg)
            boardstr = repr(self.board)
            for msg in boardstr.split("\n"):
                self.log(str(datetime.now()) + ": " + msg)
            self.update_btle()
            # Still placing tiles, but next time the button is pressed we just want to play!
            self.game_state = self.STATE_PLAYING
        
        elif self.game_state == self.STATE_PLAYING:
            # Use only one shot of randomness, since otherwise the two will be related.
            dices = self.get_random_int(0, 36)
            dice1 = dices % 6
            dice2 = dices / 6
            
            self.append_httpcmd("DICE_SET", dice1+1, dice2+1)
            msg  = str(datetime.now())
            msg += ": Button released! Dice faces: %d, %d" % (dice1+1, dice2+1)
            self.log(msg)
            
            dice_sum = dice1 + dice2
            self.stats[dice_sum] += 1
            self.update_graph()
            #Highlight selected tiles.
            self.board.update_state(dice1 + dice2 + 2, None)
            self.update_btle()
        
    def update_graph(self):
        graphdata = {}
        for dice, count in enumerate(self.stats):
            graphdata[dice+2] = count
        self.append_httpcmd("UPDATE_GRAPH", graphdata)
        
    def log(self, msg):
        self.append_httpcmd("LOG", msg)
        with open(config.settings['logfile'], 'a') as logfile:
            logfile.write(msg + '\n')
    
    def append_httpcmd(self, cmd, *args):
        """ Append a command to be send to the webbrowser """
        self.httpcmdobject.append({'command' : cmd, 'args' : args}) 
    
    def update_btle(self):
        """ Append a command to be send to the webbrowser """
        self.btlecmdobject.append(self.board.get_string())

def main(args):
    
    # Create objects for communication between python-threads
    # (Due to the GIL, so we can safely read-modify-write
    #  these lists from all threads)
    http_cmds = []
    btle_cmds = []
        
    game = KolonistenVanFS(http_cmds, btle_cmds)
    
    Handler = MakeHandlerClass(http_cmds)
    server = ThreadedHTTPServer(('localhost', 8080), Handler)
    server.cmds = http_cmds
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    
    btle = BTLE(btle_cmds)
    btle.daemon = True
    btle.start()
    
    while True:
        time.sleep(1)
        game.gpio_down()
        time.sleep(1)
        game.gpio_up()
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
