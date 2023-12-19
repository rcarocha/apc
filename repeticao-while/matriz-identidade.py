#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 18:17:48 2023

@author: rcarocha
"""

dimensao = 10

for linha in range(dimensao):
    for coluna in range(dimensao):
        if linha == coluna:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()