# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
inteiros = []
pares = []
impares = []
for c in range(20):
  num = int(input('Digite 20 valores inteiros: \n'))
  inteiros.append(num)
  if num%2 == 0:
    pares.append(num)
  else:
    impares.append(num)
print('Os números foram: ', inteiros)
print('Os números pares foram: ', pares)
print('Os números ímpares foram: ', impares)