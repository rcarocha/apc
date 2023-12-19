#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 06:49:46 2023

@author: rcarocha
"""

d1 = 1  # face do dado 1
d2 = 1  # face do dado 2
while d1 <= 6:
    while d2 <= 6:
        print("T:", d1, ",", d2)
        if (d1 + d2) == 7:      # soma dos dados vale 7
            print(d1, ",", d2)
        d2 = d2 + 1
    d2 = 1
    d1 = d1 + 1    
