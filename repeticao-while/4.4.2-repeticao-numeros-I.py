#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QA-4.4.2 - Escreva um código em Python, que imprima a sequência de numeros abaixo, a partir de um número armazenado na variável n, limite dos algarismos utilizados (no exemplo, 5)

1
12
123
1234
12345

"""

"""
n = 5
i = 1
while i <= n:
    print(i, end="")
    i = i + 1
"""
limite = 15
linha = 1
while linha <= limite:
    n = linha
    i = 1
    while i <= n:
        print(i, end="")
        i = i + 1
    print()
    linha = linha + 1

