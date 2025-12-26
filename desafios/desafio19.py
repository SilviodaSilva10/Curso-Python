'''
Aluguer de carro
custo por dia R$ 60 e R$ 0,15 por km rodados
crie um progrma que calcula e determina o preço à pagar
'''

dia = int(input('Quantos dias ? : '))
km = float(input('Quantos km? : '))

v1 =float( dia * 60) 
v2 =float( 0.15 * km)

pagar = v1 + v2 

print('O valor a pagar é de R$ {}'.format(pagar))