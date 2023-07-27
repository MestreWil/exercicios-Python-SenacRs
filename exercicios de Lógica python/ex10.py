#Faça um Programa que leia dois vetores com 10 elementos cada. 
# Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
vetorA = []
vetorB = []
vetorAB = []
for c in range(3):
  vetorA.append(input('Digite os elementos do vetor A: \n'))
for c in range(3):
  vetorB.append(input('Digite os elementos do Vetor B: \n'))
vetorAB.append(vetorA + vetorB)
print('Elementos do vetor A: {}\nElementos do vetor B: {}\nElementos do vetor AB: {}'.format(vetorA, vetorB, vetorAB))