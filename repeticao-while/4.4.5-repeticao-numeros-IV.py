#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QA-4.4.5 - Escreva um código em Python, que imprima a sequência de numeros 
abaixo, a partir de um número armazenado na variável n, limite dos algarismos 
utilizados (no exemplo, 15)

1
2  3
4  5  6
7  8  9  10
11 12 13 14 15

"""

import math

n = 15


#salto = 1
#for i in range(1, n+1):
#    print(i, end=" ")

inicio = 1
fim  = 15

num = 1
for i in range(1, int(math.sqrt(n) + 1)):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

"""
for tamanho_coluna in range(1,int(math.sqrt(fim))):
    
    for i in range(inicio, tamanho_coluna):
        print(i, end=" ")
    inicio = tamanho_coluna
"""