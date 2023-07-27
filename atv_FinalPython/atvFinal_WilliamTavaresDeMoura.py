#Lógica de programação
# Seu nome aqui: William Tavares de Moura.
# Competências a serem avaliadas:
# - Saber interpretar corretamente o que foi pedido;
# - Desenvolver uma solução viável para o problema proposto;
# - Saber utilizar os comandos/funções vistos durante o semestre;
# - Saber utilizar listas
lst_nome = []
lst_idade = []
lst_peso = []
lst_altura = []
imc = []
print('-'*30)
print('Cadastro de dados de Alunos')
print('-'*30)
while True:
  menu = 0
  try:
    while menu not in (1, 2, 3, 4, 5, 9):
      menu = int(input('Digite uma das opções abaixo:\n[ 1 ] Incluir Aluno\n[ 2 ] Listar todos alunos e seus dados\n[ 3 ] Listar os dados de um aluno\n[ 4 ] Listar os dados de todos  alunos de uma determinada Idade\n[ 5 ] Excluir  um aluno\n[ 9 ] Fim \n')) 
  except:
    print('\nOPS. SOMENTE as opções do menu podem ser selecionadas.\n')
  if menu == 1:
    lst_nome.append(str(input('Nome do Aluno: ')).capitalize())
    lst_idade.append(int(input('Idade do Aluno: ')))
    peso = float(input('Peso do Aluno: '))
    lst_peso.append(peso)
    altura = float(input('Altura do Aluno: '))
    lst_altura.append(altura)
    calculoIMC = peso /(pow(altura, 2))
    imc.append(calculoIMC)
  elif menu == 2:
    print('-'*60)
    print('Tabela de Dados de pessoas cadastradas')
    print('-'*60)
    print(f'{"Aluno":<10}{"Idade":<2}{"Peso(KG)":>10}{"Altura(Metros)":>15}{"IMC":>15}')
    for dadosTotais in range(len(lst_nome)):
      print(f'{lst_nome[dadosTotais]:<10}{lst_idade[dadosTotais]:<2}{lst_peso[dadosTotais]:>12}{lst_altura[dadosTotais]:>12}{imc[dadosTotais]:>20.2f}')
    print('-'*60)
  elif menu == 3: 
    nome = str(input('Digite o nome o aluno que deseja encontrar: ')).capitalize()
    if nome in lst_nome:
      print('-'*60)
      print(f'{"Alunos":<10}{"Idade":<2}{"Peso(KG)":>10}{"Altura(Metros)":>15}{"IMC":>15}')
      print(f'{lst_nome[lst_nome.index(nome)]:<10}{lst_idade[lst_nome.index(nome)]:<2}{lst_peso[lst_nome.index(nome)]:>10}{lst_altura[lst_nome.index(nome)]:>15}{imc[lst_nome.index(nome)]:>20.2f}')
      print('-'*60)
    else:
      print(f'\nNenhum aluno com o nome "{nome}" foi encontrado cadastrado.\n')
  elif menu == 4:
    def encontrar_idades(valores, alvo):
      return [indice for indice, valor in enumerate(valores) if valor == alvo]
    try:
      idade = int(input('Digite a idade dos alunos que deseja saber: '))
    except:
      print('Por favor, digite apenas a idade que deseja encontrar. (SEM LETRAS)')
    if idade in lst_idade:
      indices = encontrar_idades(lst_idade, idade)
      print('-'*60)
      print(f'{"Alunos":<10}{"Idade":<2}{"Peso(KG)":>10}{"Altura(Metros)":>15}{"IMC":>15}')
      print('-'*60)
      for i in range(len(indices)):
        print(f'{lst_nome[indices[i]]:<10}{lst_idade[indices[i]]:<2}{lst_peso[indices[i]]:>10}{lst_altura[indices[i]]:>15}{imc[indices[i]]:>20.2f}')
      print('-'*60)
    else:
      print('\nNenhum aluno com essa idade foi encontrado!\n')
  elif menu == 5:
    excluirAluno = str(input('Digite o nome o aluno que deseja excluir os dados: ')).capitalize()
    if excluirAluno in lst_nome:
      print('-'*60)
      print(f'{"Alunos":<10}{"Idade":<2}{"Peso(KG)":>10}{"Altura(Metros)":>15}{"IMC":>15}')
      print(f'{lst_nome[lst_nome.index(excluirAluno)]:<10}{lst_idade[lst_nome.index(excluirAluno)]:<2}{lst_peso[lst_nome.index(excluirAluno)]:>10}{lst_altura[lst_nome.index(excluirAluno)]:>15}{imc[lst_nome.index(excluirAluno)]:>20.2f}')
      print('-'*60)
      excluir = ' '
      while excluir not in('SsNn'):
        excluir = str(input('Deseja realmente excluir esse aluno? [S/N]\n'))[0]
      if excluir in 'Ss':
        indiceApagar = int(lst_nome.index(excluirAluno))
        lst_nome.pop(lst_nome.index(excluirAluno))
        lst_idade.pop(indiceApagar)
        lst_peso.pop(indiceApagar)
        lst_altura.pop(indiceApagar)
        imc.pop(indiceApagar)
    else:
      print(f'\nNenhum aluno com o nome "{excluirAluno}" foi encontrado cadastrado.\n')
  else:
    if menu == 9:
      print('-='*30)
      print('Programa FINALIZADO. Volte sempre')
      print('-='*30)
      break