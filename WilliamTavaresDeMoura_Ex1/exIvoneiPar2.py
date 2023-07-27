continuar = 'S'
nome = ''
nomeMenor = ''
menor = 0
contador = 0
while continuar != 'N':
    nome = input('Digite seu nome:\n')
    salario = float(input('Digite seu salario:\n'))
    contador += 1
    
    if contador == 1:
      menor = salario
      nomeMenor = nome
    
    else:
      if salario < menor:
          menor = salario
          nomeMenor = nome
    
    continuar = str(input('Deseja continuar? S - Sim / N - Não \n ')).upper()

print('O menor salario foi R${}, do {}'.format(menor, nomeMenor))