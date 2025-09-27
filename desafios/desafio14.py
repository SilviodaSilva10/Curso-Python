'''
Conversor de moeda mostrar o valor na carteira e mostrar quantos dollares podes comprar
'''
d = float(input('Quantos tens na carteira? : '))

conv = d/3.37

print('com R$ {:.2F} tu podes comprar $ {:.2F}'.format(d,conv))