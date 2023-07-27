#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
# Imprima a idade e a altura na ordem inversa a ordem lida
todasIdade = []
todasAltura = []
for pessoas in range(1, 6):
  todasIdade.append(int(input('Digite a idade da {}ª pessoa:\n'.format(pessoas))))
  todasAltura.append(float(input('Digite a altura da {}ª pessoa:\n'.format(pessoas))))
print('Idades na ordem normal: {}\nIdades na ordem inversa: {}'.format(todasIdade,todasIdade[::-1]))
print('Alturas na ordem normal: {}\nAlturas na ordem inversa: {}'.format(todasAltura,todasAltura[::-1]))