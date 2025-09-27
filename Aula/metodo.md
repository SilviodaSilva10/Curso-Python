# Metódos 

Os metodos são funções permitem realizar uma determinda operação em um objecto:

### Conversão

```
     int() -> transforma caracteres alfanumericos e numeros reias para numero inteiro.

     float() -> transforma caracteres alfanumericos e numeros inteiros para numero reias. 
     str() -> transforma qualquer caracter em string  

     ex.: n1 =input('Digite um numero')

     ex.: n1=float(n1)
        print(n1)
     ex.: n1=inteiro(n1)
        print(n1)
     ex.: n1=str(n1)
        print(n1)

     >>>>
     2.0
     2
     '2'

```

### isxxx()

O is quando combinado com algumas plavras ver par verificar uma terminda informação, retornando valor true ou false.

```
exemplo:

'''
Faça um programa que leia alo pelo teclado e mostra na tela
o seu tipo primitivo e todas as informaçoes possiveis sobre ela
'''

coisa= input('Digite qual quer coisa: ')
print('Digitaste {}'.format(coisa))

print('É do tipo {}'.format(type(coisa)))
print('É alfabetico: {}'.format(coisa.isalpha()))
print('É numerico: {}'.format(coisa.isnumeric()))
print('É digito de 0-9: {}'.format(coisa.isdigit()))
print('É alfanumerico: {}'.format(coisa.isalnum()))
print('Todos os caracteres são minúsculo: {}'.format(coisa.islower()))
print('Todos os caracteres são maiúsculo: {}'.format(coisa.isupper()))
print('String vazia: {}'.format(coisa.isspace()))
print('Esta capitalizada: {}'.format(coisa.istitle()))

```