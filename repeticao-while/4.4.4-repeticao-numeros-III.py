#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QA-4.4.4 - Escreva um código em Python, que imprima a sequência de numeros abaixo, a partir de um número armazenado na variável n, limite dos algarismos utilizados (no exemplo, 5)

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""

limite = 15
linha = 1
while linha <= limite:
    n = linha
    i = limite - linha + 1
    while i >= 1:
        print(i, end=" ")
        i = i - 1
    print()
    linha = linha + 1
