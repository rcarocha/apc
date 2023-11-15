""" 3
        LEIA(n)
        soma = 0
        numero = 1
        ENQUANTO numero <= n
            soma = soma + numero
            numero = numero + 1
        ESCREVA(soma)
"""
n = int(input("Digite n:"))
soma = 0
numero = 1
while numero <= n:
    numero = numero + 1
    soma = soma + numero
print(soma)
