# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
listaNumeros = []
for c in range(10):
  listaNumeros.append(int(input('Digite dez números inteiros: \n')))
print('A ordem inversa ficou: {}'.format(listaNumeros[::-1]))