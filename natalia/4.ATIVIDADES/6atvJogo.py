import os, random, time

num_escolhido = random.randint(1,100)
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