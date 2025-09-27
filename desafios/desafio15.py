'''
Faça um algoritmo que leia a largura e altura de uma parede em metros.
calcula a sua área e a quantidade de tinta para pintá-la.  Sabendo que 
cada litro de tinta, pinta uma área de 2m**2 
'''

h = float(input('Digite a altura: '))
l = float(input('Digite a largura: '))

a = l * h

tinta = a/2

print('A área de {}x{} é de {}m^2'.format( h, l, a))
print('Será necessario ter {}L de tinta '.format(tinta))