# Faça um Programa que peça as quatro notas de 10 alunos, 
# calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
mediasGerais = []
aprovados = 0

for alunos in range(1, 11):
    media = 0
    for notas in range(1, 5):
        media += float(input('Digite a {}ª nota do {}ª aluno:\n'.format(notas, alunos)))
    media /= 4
    mediasGerais.append(media)
    if media >= 7:
        aprovados += 1

print("\nA média dos alunos foi:")
for c in range(10):
    print('Aluno {}: {:.2f}'.format(c+1, mediasGerais[c]))

print('\nTiveram {} alunos que obtiveram média maior ou igual a 7.'.format(aprovados))