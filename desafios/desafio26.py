'''
Nome completo
'''

nome = input('Insira seu nome completo: ')

print('{}'.format(nome.upper()))
print('{}'.format(nome[:].lower()))

print('o teu nome tem {} letras'.format( len(nome) - nome.count(' ')))
nome = nome.split()
print('O teu 1º nome tem {} letras'.format(len(nome[0])))