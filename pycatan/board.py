#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  board.py
#  
#  Copyright 2016 Tom van Leeuwen <tom@smokie>
#  
#  Python object representing a Catan board. 
#   
import random # Will still be seed-ed by time.time(), so still affected by the button-press.
import time

import config
import copy
from tile import Tile

class Board(object):
    def __init__(self):
        self.tiles = None
        self.init()
    
    def init(self):
        """ Updates the LED state.
            @param highlight_number:    If equal to our own number, highlight the tile.
            @param highlight_resource:  If equal to our own resource, highlight the tile.
        """
        random.seed(time.time())
        while not self._verify():
            self.tiles = []
            tile_values = copy.copy(config.Tile_values)
            tile_resources = copy.copy(config.Resource_list)
            random.shuffle(tile_values)
            # Get the woestijn out of the resources before shuffling
            woestijn = tile_resources.pop(0)
            random.shuffle(tile_resources)
            # Put the woestijn at the place of value 0.
            tile_resources.insert(tile_values.index(0), woestijn)
            
            for tile_idx, tile_value in enumerate(tile_values):
                self.tiles.append(Tile(tile_value, tile_resources[tile_idx]))
        
    def __repr__(self):
        retval = "Tile Configuration:"
        for tile_id, tile in enumerate(self.tiles):
            retval += "\nTile: %d, Number: %d, resource: %s " % (tile_id, tile.number, tile.resource)
        return retval
    
    def _verify(self):
        if self.tiles == None:
            return False
        if len(self.tiles) != config.NB_TILES:
            return False
        
        for tile_id, tile in enumerate(self.tiles):
            if tile.number in config.disallow_adjecent:
                for tile_adjecent in config.adjecent_tiles[tile_id]:
                    if self.tiles[tile_adjecent].number in config.disallow_adjecent:
                        return False
        return True
        
    
    def update_state(self, highlight_number, highlight_resource, place=False):
        """ Updates the LED state.
            @param highlight_number:    If equal to our own number, highlight the tile.
            @param highlight_resource:  If equal to our own resource, highlight the tile.
        """
        for tile in self.tiles:
            tile.update_state(highlight_number, highlight_resource, place=False)
        
    def get_string(self):
        return "".join(tile.get_string() for tile in self.tiles)

def test():
    
    # Simply get the strings in a few situations.
    # No checking if the string is correct.
    board = Board()
    place = board.get_string()
    assert len(place) == config.NB_COLORS * config.NB_LEDS * config.NB_TILES
    
    board.update_state(None, None)
    dimmed = board.get_string()
    assert len(dimmed) == config.NB_COLORS * config.NB_LEDS * config.NB_TILES
    
    board.update_state(7, "Bremsenspriets")
    bremsen_and_seven = board.get_string()
    assert len(bremsen_and_seven) == config.NB_COLORS * config.NB_LEDS * config.NB_TILES
    
    board.update_state(7, None)
    seven = board.get_string()
    assert len(seven) == config.NB_COLORS * config.NB_LEDS * config.NB_TILES
    
    board.update_state(None, "Bremsenspriets")
    bremsen = board.get_string()
    assert len(bremsen) == config.NB_COLORS * config.NB_LEDS * config.NB_TILES
    
    board.update_state(6, "Carbon")
    carbon_and_six = board.get_string()
    assert len(carbon_and_six) == config.NB_COLORS * config.NB_LEDS * config.NB_TILES
    

if __name__ == '__main__':
    test()
