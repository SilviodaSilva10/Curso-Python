nome = input('Insira o seu nome completo: ').strip()
nome = nome.split()
print('O teu primeiro nome é : {}'.format(nome[0]))
print('O teu ultimo nome é : {}'.format(nome[len(nome)-1]))
