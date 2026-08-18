idade = int(input('Digite sua idade: '))

if (idade <=12):
    print(f'Criança')
elif (idade <=18):
    print(f'Adolescente')
elif (idade <=60):
    print(f'Adulto')
else:
    print(f'Idoso')