num = int(input('Insira um numero com 4 digitos: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezenas: {}'.format(d))
print('Centenas: {}'.format(c))
print('milhar: {}'.format(m))

