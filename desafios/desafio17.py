'''
Faça um programa que leia o preço de um produto e mostra 
o seu novo salário com um aumento de 15%
'''
s = float(input('Insira o teu salário: '))
novo = s + (15*s/100)

print('O teu novo slário é de {}'.format(novo))
