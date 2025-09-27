'''
Faça um algoritmo que leia o preço de um produtoe mostre o seu novo preço
com 5% de descontos
'''

preco = float(input('Insira o preco dos produto: '))

novo = preco - 5 * preco/100

print('O novo preço com desconto de 5% é de R$ {}'.format(novo))