
import os
os.system('cls, clear')


while True:
    try:
        print ("===MENU===\nTABUADA\n===========\n")
        n = int(input("Digite seu numero: "))

        for i in range (10):
            i+=1
            print(f'{n} x {i} = {n*i}')
        break

    except:
        print("Erro! Só numeros.")