#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  config.py
#  
#  Copyright 2016 Tom van Leeuwen <tom@smokie>
#  
NB_COLORS = 3
NB_LEDS = 21
NB_TILES = 19


playlist = ["dingdong.mp3", "ring.mp3"]

settings = {
        'hash_rnd' : True,
        'logfile'  : '/tmp/catan.log'
        }

Tile_values = [0, 2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]
Resource_count = {
    "Woestijn"          : 1, 
    "Bremsenspriets"    : 4, # Wol,
    "Carbon"            : 4, # Hout
    "Ziptie"            : 4, # Graan
    "Rozebutt"          : 3, # Steen
    "Alu_7075"          : 3, # Erts
}

# These numbers are multiplied by the "resources".
dimmed_intensity        = 0.1
place_intensity         = 0.25
highlighted_intensity   = 1.0

SEG_OFF = [0,0,0]
SEG_ON  = [255, 255, 255]

# 0 is the woestijn.
# We should make 6 and 8 red.
Number_leds = {
    0  : SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF, 
    2  : SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_ON  + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF, 
    3  : SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_ON  + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF, 
    4  : SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_ON  + SEG_ON  + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF, 
    5  : SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_ON  + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF, 
    6  : SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_ON  + SEG_OFF + SEG_ON  + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF, 
    8  : SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_ON  + SEG_ON  + SEG_ON  + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF, 
    9  : SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_ON  + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF, 
    10 : SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_ON  + SEG_OFF + SEG_OFF + SEG_ON  + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF, 
    11 : SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_ON  + SEG_OFF + SEG_ON  + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF, 
    12 : SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_ON  + SEG_ON  + SEG_OFF + SEG_ON  + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF + SEG_OFF, 
}

Resource_colors = {
    "Woestijn"          : [160,  80,   0],  # Geel-rood
    "Bremsenspriets"    : [128, 128,   0],  # Geel
    "Carbon"            : [255,   0,   0],  # Rood
    "Rozebutt"          : [120,  60,  60],  # Roze
    "Alu_7075"          : [  0,   0, 255],  # Wit
    "Ziptie"            : [  0, 255,   0],  # Groen
}

Resource_tiles = [True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

# 0 Starts outside, circulating to the center. Should be in-sync with the serial protocol.
adjecent_tiles = {
  0  : [     1,   11, 12],
  1  : [ 0,  2,   12, 13], 
  2  : [ 1,  3,   13],
  3  : [ 2,  4,   13, 14],
  4  : [ 3,  5,   14],
  5  : [ 4,  6,   14, 15],
  6  : [ 5,  7,   15],
  7  : [ 6,  8,   15, 16],
  8  : [ 7,  9,   16],
  9  : [ 8, 10,   16, 17],
  10 : [ 9, 11,   17],
  11 : [10, 12,   0, 17],
  12 : [11, 13,   0, 1, 17, 18],
  13 : [12, 14,   1, 2, 3, 18],
  14 : [13, 15,   3, 4, 5, 18],
  15 : [14, 16,   5, 6, 7, 18],
  16 : [15, 17,   7, 8, 9, 18],
  17 : [16, 18,   9, 10, 11, 12],
  18 : [17,       12, 13, 14, 15, 16],
}

# If the tile number is 6 or 8, it is not allowed to be adjecent to another tile that has number 6 or 8.
disallow_adjecent = [6, 8]

# Below here comes some code to convert it to easily-accessible arrays. It contains no more settings.

Resource_leds = {}
for resource, color in Resource_colors.items():
    leds = []
    for on in Resource_tiles:
        if on:
            leds += color
        else:
            leds += [0, 0, 0]
    Resource_leds[resource] = leds

Resource_list = []
for (resource, count) in Resource_count.items():
    Resource_list += [resource for _ in xrange(count)]
    
print Resource_list


for value in Resource_leds.values():
    assert len(value) == NB_LEDS * NB_COLORS
    for intensity in value:
        assert ord(chr(intensity)) == intensity

for value in Number_leds.values():
    assert len(value) == NB_LEDS * NB_COLORS
    for intensity in value:
        assert ord(chr(intensity)) == intensity

# Check if the intensity is between 0 and 1, otherwise it still won't fit in a byte...
assert dimmed_intensity >= 0.0 and dimmed_intensity <= 1.0
assert highlighted_intensity >= 0.0 and highlighted_intensity <= 1.0

# Check if the adjecent tile array agrees with itself.
for tile, adjecent in adjecent_tiles.items():
    for other_tile, other_adjecent in adjecent_tiles.items():
        if other_tile in adjecent:
            assert tile in other_adjecent # Adjecent tile mapping incorrect
        else:
            assert tile not in other_adjecent # Adjecent tile mapping incorrect
    assert tile not in adjecent # Can't be adjecent to ourselves.
