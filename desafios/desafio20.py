'''
Crie um programa que leia um numero real qualquer pelo
teclado e mostre na tela a sua porção inteira 
'''
from math import trunc
nu = float(input('insira um numero real: '))
print('Aporçaõ inteira de {} é {}'.format(nu,trunc(nu)))