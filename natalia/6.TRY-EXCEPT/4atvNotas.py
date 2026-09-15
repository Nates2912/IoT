
import os
os.system('cls, clear')

notas = []

while True:
    try:
        print ("|NOTAS|")
        for i in range (3):
            entrada = int(input(f"Digite a {i+1}ª nota: "))
            notas.append(entrada)
        media = sum(notas)/len(notas)
        
        if media>=7:
            print("APROVADO!")
        elif media < 5:
            print("REPROVADO")
        else:
            print("RECUPERAÇÃO")
        break

    except:
        print("Erro! Só numeros.")