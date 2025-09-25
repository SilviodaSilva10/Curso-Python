# Input

É uma das funções principais do Python ela permite a interação do usuario com o sistema permitindo ao usuario fornecer dados para serem processados pelo sistema.

### input()

```
nome = input('Insira seu nome')
```

O input() por si só recebe dados do tipo string(str) assim permitindo a entrada de caracteres alfanumericos.
```
nome= input('Digite seu nome: ')
print(nome)

>>> Sílvio da Silva
```

Sempre que for feita uma operação matemáticas com dados deigitados pelo usuario se não forem convertidos para um valor int() ou float() o seu resultado será concatenado ou desconcatenado

Incorrecto:
```
n1 = input('insira o 1º: ')
n2 = input('insira o 2º: ')

s = n1 + n2

print(f'O resultado é: {s}')

<<<<execução>>>>
insira o 1º: 2
insira o 2º: 3
>>> O resultado é: 23
```

Correcto:
```
n1 = int(input('insira o 1º: ')) #n1 = float(input('insira o 1º: '))
n2 = int(input('insira o 2º: ')) #n2 = float(input('insira o 2º: '))

s = n1 + n2

print(f'O resultado é: {s}')

<<<<execução>>>>
insira o 1º: 2
insira o 2º: 3
>>> O resultado é: 5
```

