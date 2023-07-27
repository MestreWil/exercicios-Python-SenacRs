#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
a = []
for c in range(1, 11):
  num = a.append(pow(int(input('Digite o {}ª valor: '.format(c))), 2))
print('A soma dos quadrados dos números que vc digitou fica: {}'.format(sum(a)))