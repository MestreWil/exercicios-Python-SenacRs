x = 'S'
cont = 0
maior = 0
menor = 0
nomeMaior = ''
nomeMenor = ''

while x != 'N':
    nome = input('Digite seu nome:')
    z = int(input('Digite seu salario: '))
    cont += 1
    
    if cont == 1:
       maior = z
       menor = z
       nomeMaior = nome
       nomeMenor = nome
    else:
        if z > maior:
            maior = z
            nomeMaior = nome
        if z < menor:
            menor = z
            nomeMenor = nome

    x = str(input('Deseja continuar? S - Sim / N - Não  ')).upper()

print('O MAIOR salario digitado foi do {} que recebe R${}.'.format(nomeMaior,maior))
print('O MENOR salario digitado foi do {} que recebe R${}.'.format(nomeMenor,menor))