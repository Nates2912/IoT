# Gere um número aleatório entre 1 e 20. Em um while True , peça palpites até que o usuário acerte.
# Informe se cada palpite foi maior ou menor que o número sorteado, conte as tentativas e encerre com break quando houver acerto.

import os, random, time
os.system('cls, clear')

num_escolhido = random.randint(1,20)
# i = tentativas
i = 0

while True:
    numero = int(input("Digite o número secreto"))
    i+=1
    if (numero == num_escolhido):
        print(f'Você acertou com {i} tentativas!')
        break
    
    elif(num_escolhido > numero):
        print(f"O numero secreto é MAIOR - {i} Tentativas")
        time.sleep(2)
        os.system('cls' or 'clear')
        
    elif(num_escolhido < numero):
        print(f"O numero secreto é MENOR - {i} Tentativas")
        time.sleep(2)
        os.system('cls' or 'clear')