'''
Escreva um programa que leia um valor em metro e o exiba convertido em centimetrs
e milimetros
'''
m = float(input('Insira o valor em metros: '))

print('Convertendo valor digitado {}m \nCentimetros: {}cm \nMilimetros: {}mm'.format(m, (m*100), (m*1000)))