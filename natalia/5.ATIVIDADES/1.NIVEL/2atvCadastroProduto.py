# Crie uma lista vazia. Utilize for com range(5) para pedir cinco produtos ao usuário e adicionar cada um com append(). 
# Ao final, exiba a lista completa e a quantidade de produtos cadastrados.

import os
os.system('cls, clear')

produtos = []

print ("==========MENU===========\nCADASTRAMENTO DE PRODUTOS\n=========================\n")

for i in range (5):
    cadastro = input(f"Insira o nome do {i+1}º produto: ")
    produtos.append(cadastro)

print (f"\n=====RESULTADOS=====\n  | PRODUTOS: {produtos}! | \n====================")