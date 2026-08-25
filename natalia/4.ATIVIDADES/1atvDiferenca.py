# Crie um programa que lê uma lista de 10 números e conta a quantidade de
# números positivos e a quantidade de números negativos, e mostra o vetor
# com os negativos e o a soma dos positivos?

num = []
pos = []
neg = []

print ("========MENU=======\nInforme os numeros.\n===================")

for i in range (10):
    numeros = float(input(f"Informe o {i+1}º número: "))
    
    if numeros > 0:
        pos.append(numeros)
    elif numeros < 0:
        neg.append(numeros)
    else:
        num.append(numeros)


print (f"|==========RESULTADOS==========|\n|A soma dos positivos é: {sum(pos)}   |\n|Os números negativos são: {len(neg)}   |\n|==============================|")

        