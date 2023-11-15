""" 6
Escreva um programa que leia a nota de cada aluno (**até** que seja passado um valor **negativo**), e calcule a média das notas.

Elabore o seu código a partir da combinação dos seguintes trechos de código na próxima tabela, indicando a indentação necessária.

Elabore o código Python em três etapas:

1. Implemente a leitura das notas dos alunos, de acordo com o critério de parada.
2. Reflita sobre as variáveis (informações) que você precisa para fazer o cálculo desejado.
3. Introduza no código variáveis, atualizações e cálculos que permitam refletir o cálculo imaginado no item anterior.
"""

<!--
```Python
nota = float(input("Digite a nota: "))
n_notas = 0
soma_notas = 0
while nota >= 0:
   n_notas = n_notas + 1
   soma_notas = soma_notas + nota
   nota = float(input("Digite a nota: "))
if n_notas > 0:
   print("Media das notas = ", soma_notas/n_notas)
else:
   print("Não há media a calcular!")
```
-->
