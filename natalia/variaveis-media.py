uni1 = float(input('Digite a nota da 1ª Unidade: '))
uni2 = float(input('Digite a nota da 2ª Unidade: '))
uni3 = float(input('Digite a nota da 3ª Unidade: '))

media = (uni1 + uni2 +uni3) / 3

if(media>=5):
    print(f'A sua média é {media:.1f} - você foi APROVADO!')
else:
    print(f'A sua média é {media:.1f} - você foi REPROVADO!')