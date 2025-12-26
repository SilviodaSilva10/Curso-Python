import random
no1=input('Digite o 1º nome: ')
no2=input('Digite o 2º nome: ')
no3=input('Digite o 3º nome: ')
no4=input('Digite o 4º nome: ')
lista = [ no1, no2, no3, no4 ]

print('O aluno escolhido é: {}'.format(random.choices(lista)))