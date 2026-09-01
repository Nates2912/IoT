# 05 Lista de convidados com palavra de saída
# Crie uma lista vazia e utilize while True para receber nomes.
# Cada nome deve ser incluído com append().
# Quando o usuário digitar 'fim' , encerre com break.
# Depois, organize os nomes em ordem alfabética e mostre a lista e sua quantidade.

import os
os.system('cls, clear')

convidados = []

print ("=====================MENU======================\nAdicione convidados! Digite FIM quando terminar!\n===============================================")

while True:
    nomes = input("Digite o nome do convidado: ")
    
    if (nomes!='FIM'):
        convidados.append(nomes)
    
    else:
        break
        
convidados.sort()

print ("===========MENU==========")
print(f'| LISTA DE CONVIDADOS: {convidados} \n| QUANTIDADE: {len(convidados)} ')
