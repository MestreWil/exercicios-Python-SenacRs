#Este exercício vale como presença da aul do sábado letivo de 15/0402023

#Faça um programa que, para um número indeterminado de pessoas: leia a idade de cada uma, sendo que a idade 0 (zero) 
#indica o fim da leitura e não deve ser considerada. A seguir calcule: 

'''a quantidade de pessoas;
a idade média do grupo;
a menor idade e a maior idade'''

maiorMenor = []
while True:
    
    idade = int(input('Digite sua idade ou 0 para finalizar:\n'))
    
    if idade == 0:
        break
    
    maiorMenor.append(idade)
    media = sum(maiorMenor)/len(maiorMenor)
    maiorMenor.sort()
print('Quantidade de pessoas analisadas: {}\n'.format(len(maiorMenor)))
print('As idades foram: {}\n'.format(maiorMenor))
print('A media das idades foi: {:.2f}\n'.format(media))
print('Maior idade = {} Idade menor = {}'.format(maiorMenor[-1],maiorMenor[0]))
print('FIM')