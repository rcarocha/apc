#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 11:00:58 2023

@author: rcarocha

n = 5
print('[',end="")
for e in range(n-1):
    print(" ",end="") # print contem um caracter em branco
print(']')

[     ] - (5 espaços)
=[    ] - (4 espaços)
[   ] - (3 espaços)
[  ] - (2 espaços)
[ ] - (1 espaços)
[]

n = 5
for k in range(1,n+1):
    print(k,end="")

123456
=12345
1234
123
12
1
0123456
012345
01234
0123
012
01
não imprimirá nada
15
16
05
06

n = 5
for k in range(n-1,0,-1):
    print(k,end="")

54321    
=4321
321
21
1
543210
43210
3210
210
10
0
543210-1
43210-1
3210-1
210-1
10-1
0-1
-1
não imprimirá nada

"""



n = 5

for i in range(1,n+1):
    
    for e in range(n-i):
        print(' ',end="")
    
    lim = i
    for k in range(1,lim+1):
        print(k,end="")
    for k in range(lim-1,0,-1):
        print(k,end="")
    print()
        
    
n = 5
print('[',end="")
for e in range(n-1):
    print(" ",end="") # print contem um caracter em branco
print(']')

n = 5
for k in range(1,n+1):
    print(k,end="")
    
n = 5
for k in range(n-1,0,-1):
    print(k,end="")
    
"""

# Saida 1
    1
   121
  12321
 1234321
123454321 

# Saida 2
     0
    010
   01210
  0123210
 012343210
01234543210

# Saida 3
     123454321
     
# Saida 4
     01234543210
     
# Saida 5
12345
4321

# Saida 6
012345
43210

"""