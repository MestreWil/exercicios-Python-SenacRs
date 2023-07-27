#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
from math import prod

numeros = []
for c in range(5):
  num = numeros.append(int(input('Digite cinco números inteiros: \n')))
print('Os números digitados foram: ',numeros)
print('A soma desses números é igual a: {}'.format(sum(numeros)))
print('A multiplicação desse números é igual a: {}'.format(prod(numeros)))
