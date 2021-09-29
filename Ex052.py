"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""

num = int(input('Digite um número: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[31m', end=' ')
        cont = cont + 1
    else:
        print('\033[97m', end=' ')
    print(f'{c}', end=" ")
print(f'\n\033[mO número {num} foi divisível {cont} vezes')
if cont == 2:
    print('É PRIMO')
else:
    print('NÃO É PRIMO')

