# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
letras = []
i = 1
while i <= 10:
    letras.append(input("Letra: "))
    i += 1
i = 0
cont = 0
while i <= 9:
    if letras[1] not in 'aeiou':
        cont += 1
    i += 1
print ("Foram lidos {} consoantes".format(cont))
