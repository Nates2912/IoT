# 04 Contando valores pares e ímpares
# Use a lista numeros = [ 12 , 7 , 9 , 20 , 31 , 44 , 18 , 5 ] . Percorra os valores com for e conte
# quantos são pares e quantos são ímpares. Mostre as duas quantidades ao final.

import os
os.system('cls, clear')

listanumeros = [ 12 , 7 , 9 , 20 , 31 , 44 , 18 , 5 ]
quantidade = len(listanumeros)

par = 0
impar = 0

print ("===MENU===\nPAR E ÍMPAR\n===========\n")

for i in range (quantidade):
    
    if listanumeros[i] % 2 == 0:
        par += 1
    else:
        impar += 1
    
print(f'| NÚMEROS: {listanumeros}: |\n| PARES: {par}  |\n| ÍMPARES {impar} |\n')