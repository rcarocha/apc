""" 7

Construa um algoritmo  que gere os 20 primeiros da série similar à Fibonacci, considerando os dois primeiros termos fornecidos pelo usuário.

A série de Fibonacci é uma série de números em que um elemento $x_i$ é igual à soma dos dois elementos anteriores na série: $x_{i-1}$ e $x_{i-2}$.

Por exemplo, se o ususário digitar 3 e 4, a série deve ser a seguinte:

```
termo  1 2 3  4  5  6  7  8   9  10  11  12  13   14 ...
numero 3 4 7 11 18 29 47 76 123 199 322 521 843 1364 ...
```
"""

<!--
```Python
termo1 = int(input("Termo 1 da serie"))
termo2 = int(input("Termo 2 da serie"))

n_termos = 2
total_termos = 20

while n_termos < total_termos:
   prox_termo = termo1 + termo2
   print(prox_termo, end=" ")
   termo1 = termo2
   termo2 = prox_termo
   n_termos = n_termos + 1
```
-->
