import math 
a = float(input('Insira qualquer angulo: '))

a = math.radians(a)
sen= math.sin(a)
print('O sen é: {:.2f}'.format(sen))
coss= math.cos(a)
print('O cosseno é: {:.2f}'.format(coss))
tang= math.tan(a)
print('A tangente é: {:.2f}'.format(tang))
