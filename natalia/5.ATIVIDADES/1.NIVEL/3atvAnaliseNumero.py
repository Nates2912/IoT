# 03 Análise de números
# Peça seis números inteiros utilizando um laço for e armazene-os em uma lista.
# Depois, mostre a soma, o maior valor, o menor valor e os números em ordem crescente.

import os
os.system('cls, clear')

listaNumeros = []

print ("=====MENU=====\nInsira números.\n==============")

for i in range(5):
    numeros = float(input(f"Digite a {i+1}ª listaNumeros: "))
    listaNumeros.append(numeros)
    
listaNumeros.sort()

print ("=====RESULTADOS=====")
print(f'| A soma é {sum(listaNumeros):.1f}° |\n| O maior é {max(listaNumeros)}° |\n| O menor é {min(listaNumeros)}  |\n| A ordem crescente é: {listaNumeros} |\n')