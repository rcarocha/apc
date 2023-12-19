#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QA-4.4.3 - Escreva um código em Python, que imprima a sequência de numeros abaixo, a partir de um número armazenado na variável n, limite dos algarismos utilizados (no exemplo, 5)

12345
1234
123
12
1
"""

limite = 15
linha = 1
while linha <= limite:
    n = linha
    i = 1
    while i <= (limite - n + 1):
        print(i, end="")
        i = i + 1
    print()
    linha = linha + 1