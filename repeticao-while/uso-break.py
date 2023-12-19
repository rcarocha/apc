#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 06:37:27 2023

@author: rcarocha
"""

for i in range(5):
    if i == j:
        break
    for j in range (5):
        print(i, j)

segredo = 61
tentativa = int(input("Tente adivinhar o numero secreto (entre 0 e 100):"))
num_tentativas = 1
while tentativa != segredo:
    if tentativa < segredo:
        print("Você escolheu um numero muito BAIXO!")
    else:
        print("Você escolheu um numero muito ALTO!")
    tentativa = int(input("Tente adivinhar o numero secreto (entre 0 e 100):"))
    num_tentativas = num_tentativas + 1
print("Você acertou em ", num_tentativas, " tentativas.")