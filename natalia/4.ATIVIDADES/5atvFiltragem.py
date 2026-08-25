# Filtragem e Média de Dados (Processamento de Vetores)

# Enunciado: Desenvolva um programa que peça ao usuário para digitar a nota de 8
# alunos e armazene-as em uma lista. O programa deve:

# 1. Calcular e mostrar a média aritmética da turma.
# 2. Criar e exibir uma nova lista contendo apenas as notas que ficaram acima
# da média calculada.

notaAluno = []

for i in range (4):
    notas = float(input(f"Nota do {i+1}º aluno(a): "))
    notaAluno.append(notas)
    
media = sum(notaAluno) /len(notaAluno)
print (f"MEDIA DA TURMA: {media}")

notaDestaques = []

for notas in notaAluno:
    if notas > media:
        notaDestaques.append(notas)
        
print (f"NOTAS DESTAQUE: {notaDestaques}")