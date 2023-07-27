'''Escreva um programa em Python que solicite que o usuário digite um número inteiro. 
O programa deve calcular a tabuada de 10 desse número e exibir os resultados na tela. O programa deve continuar solicitando ao usuário 
que digite novos números até que o número digitado seja igual a 0, momento em que o programa deve encerrar.
O programa deve seguir os seguintes passos:
1. Solicitar que o usuário digite um número inteiro diferente de 0.
2. Caso o número digitado seja diferente de 0, calcular e exibir a tabuada do número.
3. Repetir os passos 1 e 2 até que o usuário digite o número 0.
4. Encerrar o programa.
O programa deve calcular a tabuada do número digitado usando um loop `for` que itera de 1 a 10 e multiplica cada número pelo número digitado. 
O resultado deve ser exibido na tela usando a função `print()`.
'''

while True:
  num = int(input('Digite um número inteiro para ver a tabuada dele ou 0 para parar: \n'))
  if num == 0:
    print('O programa foi finalizado!')
    break
  else:
    print('A tabuada do número {} é:'.format(num))
    for c in range(1, 11):
      #tabuada = num*c
      print('{} x {} = {}'.format(num, c, num*c))
      
