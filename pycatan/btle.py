#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  btle.py
#  
#  Copyright 2016 Tom van Leeuwen <tom@smokie>
#  
import traceback
import time
import threading

# To see if the string is changed...
import hashlib
import struct

import config
class BTLE(threading.Thread):
    def __init__(self, btlecmds, *args, **kwargs):
        self.btlecmds = btlecmds
        self.lastcmd = None
        threading.Thread.__init__(self, *args, **kwargs)
        
    def run(self):
        # Always continue.
        while True:
            try:
                # Open serial port.
                
                # Start polling until:
                # a) Timeout of 10 seconds expired (re-load the last data if available)
                # b) New data is available.
                timeout = time.time() + config.settings['btle_timeout']
                while len(self.btlecmds) == 0 and time.time() < timeout:
                    time.sleep(0.01)
                    
                # Get the most recent command. Probably the only one but we can never be sure...
                while len(self.btlecmds) > 0:
                    self.lastcmd = self.btlecmds.pop(0)
                
                if self.lastcmd == None:
                    # No command yet. Remove in real implementation.
                    print "No command yet!"
                else:
                    # Write to serial port. For now, print some hash so we can see if it is changed.
                    hashstr = hashlib.md5(self.lastcmd).digest()
                    hashint = struct.unpack("<I", hashstr[0:4])[0]
                    print "Hash of cmd: 0x%08X" % hashint
                
            except Exception as e:
                print traceback.print_exc()
        
            
