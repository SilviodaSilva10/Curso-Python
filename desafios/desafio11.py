'''
Desenvolva um progrma que leia duas notas de um aluno e calcula a media 
'''

n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))

m = (n1 +n2)/2

print('A primeira nota digita é {} \nA segunda nata digita é {} \nA sua media é {:.1f} valores'.format(n1,n2,m))