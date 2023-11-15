""" 8
Construa um algoritmo que, dado um conjunto de valores inteiros e positivos, determine o menor e o maior valor do conjunto.

O final do conjunto de valores é determinado pelo valor -1, que não deve fazer parte do conjunto.
"""

num = int(input("Numero: "))
maior = num
menor = num
while num != -1:
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    num = int(input("Numero: "))
print("Maior: ", maior)
print("Menor: ", menor)
