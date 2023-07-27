# WILLIAM TAVARES DE MOURA
listaA = []
listaB = []
finalZero = 0
# Questão 1
for disciplinas in range(5):
  listaA.append(str(input(f'Digite a {disciplinas+1}ª disciplina do 1ª semestre: ')).strip())
# Questão 2
for numeros in range(10):
  num = 0
  try:
    while num < 100 or num >500:
      num = int(input(f'Digite dez números de 100 a 500 ({numeros+1}ª): '))
    if 100<= num <=500:
      listaB.append(num)
    else:
      print('OPS. Só vale números entre 100 e 500')
  except:
    print('OPS. Só vale números entre 100 e 500')
# Questão 3
print('Escolha uma das disciplinas:')
listaA.sort(key=len)
for item in range(5):
  print(f'"{listaA[item]}" digite: [ {item+1} ]')
maior = int(input('Para saber qual tem a maior quantidade de letras e qual sua posição na lista: \n'))
if maior == 1:
  print(f'A posição na lista é {listaA.index("Lógica de Programação")}')
elif maior == 2:
  print(f'A posição na lista é {listaA.index("Fundamentos Computacionais")}')
elif maior == 3:
  print(f'A posição na lista é {listaA.index("Fundamentos de Redes de Computadores")}')
elif maior == 4:
  print(f'A posição na lista é {listaA.index("User Experience")}')
else:
  print(f'A posição na lista é {listaA.index("Desenvolvimento de Interfaces para Web")}')
# Questão 4
for item in listaB:
  if item%10==0:
    finalZero +=1
print(f'Tem {finalZero} números finalizados com o número zero na listaB.')
# Questão 5
while True:
  try:
    indice = int(input('Digite o valor de indicia para a listaB: '))
    if 0 < indice or indice > len(listaB):
      print('Por favor, digite um valor valido!')
    else:
      listaB[indice] = str(listaB[indice])
      print(f'{listaB[indice]} foi convertido para variavel string!')
      break
  except:
    print('Somente números para indicar o indice!')
# Questão 6
for nome in range(5):
  print(f'{listaA[nome][0:3]} da disciplina {listaA[nome]}')