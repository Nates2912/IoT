# Crie um programa em Python que lê uma lista de 10 nomes e sorteia um
# nome entre eles.

import os
import random

print ("==========MENU==========\nSORTEIO! Insira seu nome!\n========================\n")

nomes = []

for i in range (10):
    participante = str(input("Digite seu nome: "))
    nomes.append(participante)
    
sorteado = random.choice(nomes)

print (f"\n=========RESULTADOS=========\nO sorteado(a) é: {sorteado}!\n============================")
