# Peça ao usuário para digitar 5 temperaturas (uma por uma) e guarde-as em uma lista.
# Use um laço para a entrada de dados.
# Após a leitura, exiba:

# A maior temperatura registrada (max).
# A menor temperatura registrada (min).
# A média das temperaturas.

temperatura = []

print ("=============MENU=============")
print("Informe as temperaturas do dia.")
print ("==============================")

for i in range(10):
    temp = float(input(f"Digite a {i+1}ª temperatura: "))
    temperatura.append(temp)
    
media = sum(temperatura) /len(temperatura)
maior = max(temperatura)
menor = min(temperatura)

print ("=====RESULTADOS=====")
print(f'| O maior é {maior}° |\n| O menor é {menor}° |\n| A média é {media:.1f}° |')