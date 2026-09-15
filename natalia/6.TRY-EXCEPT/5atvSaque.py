
import os
os.system('cls, clear')


while True:
    try:
        
        print ("|SAQUE E SALDO|\n")
        saldo = float(input("Digite seu saldo: "))
        saque = float(input("Digite seu saque: \n"))

        if saldo >= saque:
            print(f"SAQUE REALIZADO COM SUCESSO!\nSALDO RESTANTE: {saldo - saque:.2f}")
            break
        
        else:
            print("SALDO INSUFICIENTE!")

    except:
        print("Erro! Só numeros.")