# Escreva um programa que leia uma lista de 5 nomes e depois exiba esses
# nomes em ordem alfabética.

print ("==========MENU==========\nSORTEIO! Insira seu nome!\n========================\n")

nomes = []

for i in range (5):
    pessoas = input("Digite seu nome: ")
    nomes.append(pessoas)
nomes.sort()

print (f"\n=====RESULTADOS=====\n  | Nomes: {nomes}! | \n====================")
