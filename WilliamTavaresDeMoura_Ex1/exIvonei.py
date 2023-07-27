'''
Faça um algoritmo que leia o nome e o salário de 5 pessoas. Após a digitação, mostre o nome e o salário da pessoa que recebe o menor salário.
Obs. Crie uma solução sem o uso de listas.
Parte 2
Altere o exercício anterior para ler o nome e o salário de um número indeterminado de pessoas.
'''
nome = ''
nomeMenor = ''
menor = 0
for c in range(1, 6):
    nome = input('Digite seu nome:\n')
    salario = float(input('Digite seu salario:\n'))
    if c == 1:
        menor = salario
    else:
        if salario < menor:
            menor = salario
            nomeMenor = nome


print('O menor salario foi R${}, do {}'.format(menor, nomeMenor))