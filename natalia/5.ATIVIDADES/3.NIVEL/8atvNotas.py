# Crie uma lista vazia. Use while True para cadastrar notas até que o usuário digite -1.
# Depois do encerramento, utilize um for para mostrar cada nota cadastrada.
# Exiba também a quantidade, a média, a maior nota, a menor nota e as notas em ordem decrescente.

import os
os.system('cls, clear')

listaNotas = []

print ("=====================MENU======================\nInsira notas! Digite -1 quando terminar!\n===============================================")

while True:
    nota = float(input("INSIRA SUA NOTA: "))
    
    
    if nota >= 0 and nota <= 10:
        listaNotas.append(nota)
        
    elif nota == -1:
        break
    
    else:
        print("NOTA INVALIDA! LEMBRE-SE: ENTRE 0 E 10!")
        
if len(listaNotas) > 0:
    print("\nNotas cadastradas:")
    for n in listaNotas:
        print(f"- {n}")
        
    listaNotas.sort(reverse=True)
    qtd = len(listaNotas)
    media = sum(listaNotas) / qtd
    
    print(f"\nQuantidade de notas: {len(listaNotas)}\nMédia das notas: {media:.2f}\nMaior nota: {max(listaNotas)}\nMenor nota: {min(listaNotas)}\nNotas em ordem decrescente: {listaNotas}")

