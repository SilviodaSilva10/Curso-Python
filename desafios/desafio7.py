'''
Faça um programa que leia alo pelo teclado e mostra na tela
o seu tipo primitivo e todas as informaçoes possiveis sobre ela
'''

coisa= input('Digite qual quer coisa: ')
print('Digitaste {}'.format(coisa))

print('É do tipo {}'.format(type(coisa)))
print('É alfabetico: {}'.format(coisa.isalpha()))
print('É numerico: {}'.format(coisa.isnumeric()))
print('É digito de 0-9: {}'.format(coisa.isdigit()))
print('É alfanumerico: {}'.format(coisa.isalnum()))
print('Todos os caracteres são minúsculo: {}'.format(coisa.islower()))
print('Todos os caracteres são maiúsculo: {}'.format(coisa.isupper()))
print('String vazia: {}'.format(coisa.isspace()))
print('Esta capitalizada: {}'.format(coisa.istitle()))