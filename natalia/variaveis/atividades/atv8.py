#imput do usuario
numero1 = int (input("Digite um numero: "))
numero2 = int (input("Digite um numero: "))
operacao = input("Escolha o operador. (+ - * /): ")

#resultados
if operacao == "+":
    adicao = numero1+numero2
    print(f"Adição: {adicao}")
    
elif operacao == "-":
    subtracao = numero1-numero2
    print(f"Subtração: {subtracao}")
    
elif operacao == "*":
    multiplicacao = numero1*numero2
    print(f"Multiplicação: {multiplicacao}")
    
elif operacao == "/":
    divisao = numero1/numero2
    print(f"Divisão: {divisao}")
    
else:
    print("Operador inválido.")




