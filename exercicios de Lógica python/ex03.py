# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
todasNotas = []
for notas in range(1, 5):
  todasNotas.append(float(input('Digite a sua {}ª notas: \n'.format(notas))))
print('Suas notas foram: {}.\nE sua média ficou: {:.2f}.'.format(todasNotas, sum(todasNotas)/len(todasNotas)))