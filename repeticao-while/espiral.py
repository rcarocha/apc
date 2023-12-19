#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 21:53:32 2023

@author: rcarocha
"""

x = 0
y = 0
min_x = 0
min_y = 0
max_x = 5
max_y = 6


while min_x < max_x and min_y < max_y:
    while y <= max_y:
       print(f'({x},{y})')
       y = y + 1
    
    y = max_y
    x = x + 1
    while x <= max_x:
       print(f'({x},{y})')
       x = x + 1
       
    x = max_x
    y = y - 1
    while y >= min_y:
       print(f'({x},{y})')
       y = y - 1
       
    y = min_y
    x = x - 1
    while x > min_x:
       print(f'({x},{y})')
       x = x - 1
       
    x = min_x + 1
    y = y + 1
       
    min_x = min_x + 1
    min_y = min_y + 1
    max_x = max_x - 1
    max_y = max_y - 1
