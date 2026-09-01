# 06 Menu de gerenciamento de tarefas
# Crie uma lista vazia e apresente continuamente o menu: 1 - Adicionar tarefa,2 - Remover tarefa, 3 - Mostrar tarefas e 0 - Sair.
# Use while True para manter o menu ativo, append() para adicionar, remove() para retirar e break para encerrar.

import os
os.system('cls, clear')

listaTarefa = []

while True:
    print("""
    NÚMERO \t AÇÕES
    1 \t ADICIONAR TAREFA
    2 \t REMOVER TAREFA
    3 \t EXIBIR TAREFA
    0 \t SAIR
    """)

    codigo = input("ESCOLHA SUA AÇÃO: ")

    match codigo:
        case "1":
            tarefa = input("Insira sua tarefa: ")
            listaTarefa.append(tarefa)
            print("TAREFA ADICIONADA COM SUCESSO!")

        case "2":
            tarefaRem = input("Insira a tarefa sendo removida: ")
            if tarefaRem in listaTarefa:
                listaTarefa.remove(tarefaRem)
                print("TAREFA REMOVIDA COM SUCESSO!")
            else:
                print("TAREFA NÃO ENCONTRADA NA LISTA!")

        case "3":
            print("SUAS TAREFAS:")
            for tarefa in listaTarefa:
                print(f"- {tarefa}")

        case "0":
            print("SAINDO...")
            break

        case _:
            print("ERRO! TENTE NOVAMENTE...")