import os
os.system('cls, clear')

while True:
    try:
        numero1 = int(input("Digite seu numero: "))
        numero2 = int(input("Digite seu numero: "))
        
        total = numero1 + numero2
        
        print(f"Resultado: {total}")
        break
        
    except:
        print("Erro! Só numeros.")
        