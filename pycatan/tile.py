#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tile.py
#  
#  Copyright 2016 Tom van Leeuwen <tom@smokie>
#  
#  Python object representing a Catan tile. Properties:
#   Number: The number in the center of the tile (2 to 12)
#   Resource: A resource string (a key in the config.Resources dict)
#   
import config
import copy

class Tile(object):
    def __init__(self, number, resource):
        self.number = number
        self.resource = resource
        self.led_state = None
        self.update_state(None, None, place=True)
    
    def update_state(self, highlight_number, highlight_resource, place=False):
        """ Updates the LED state.
            @param highlight_number:    If equal to our own number, highlight the tile.
            @param highlight_resource:  If equal to our own resource, highlight the tile.
        """
        self.led_state = copy.copy(config.Number_leds[self.number])
        resource_leds = config.Resource_leds[self.resource]
        
        resource_intensity = config.dimmed_intensity
        
        if self.number == highlight_number or self.resource == highlight_resource:
            resource_intensity = config.highlighted_intensity
        
        if place:
            resource_intensity = config.place_intensity
        
        for idx, val in enumerate(self.led_state):
            self.led_state[idx] += int(resource_intensity * resource_leds[idx])
        
    def get_string(self):
        return "".join((chr(ledstate) for ledstate in self.led_state))

def test():
    
    tile = Tile(7, "Bremsenspriets")
    placing = tile.get_string()
    
    tile.update_state(None, None)
    dimmed = tile.get_string()
    
    tile.update_state(7, "Bremsenspriets")
    highlighted = tile.get_string()
    
    tile.update_state(7, None)
    assert tile.get_string() == highlighted
    
    tile.update_state(None, "Bremsenspriets")
    assert tile.get_string() == highlighted
    
    tile.update_state(6, "Carbon")
    assert tile.get_string() == dimmed
    

if __name__ == '__main__':
    test()
