numeros = [23,26,21,23,25]
nomes = ["Mav", 'Gideon','Paule', 'Zhadie', 'Ada']


# #append - Insere um novo valor no vetor, sempre na última posição.
nomes.append('Sally')
print(nomes)

# #insert - Insere um novo valor na posiçao desejada.
numeros.insert(2, 29)
print(numeros)

# #pop - Deleta um valor pela sua posição - se ficar vazio, ele remove o último.
numeros.pop()
print(numeros)

# #remove - Deleta um valor pelo seu conteúdo.
nomes.remove('Ada')
print(nomes)

# #sort - Ordena de forma crescente o vetor. Da pra organizar de forma decresente com o reverse.
numeros.sort()
print(numeros)

# #reverse - Inverte as posições do vetor
numeros.reverse()
print(numeros)

#len - Conta quantos valores existem dentro de um vetor.
quantidade = len(numeros)
print(f'A quantidade de números é {quantidade}')

#count - Conta a quantidade de um valor específico dentro de um vetor
quantidade = numeros.count()
print(f'A quantidade de números é {quantidade}')

#sum() - Soma de todos os valores do vetor.
total = numeros(sum)
print(f'A soma de números é {total}')

#max - #min - Traz o maior/menor valor do vetor.
maior = max(numeros)
menor = min(numeros)
print(f'O maior é {maior} | O menor é {menor}')
