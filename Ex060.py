"""
Faça um programa que leia um número qualquer e mostre o seu factorial.
"""
# forma mais simples usando a função factorial #
# PRIMEIRA FORMA #
from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
fatorial = factorial(n)
print(f'O fatorial de {n} é: {fatorial}')

# Forma Matemática de se fazer o fatorial #
# SEGUNDA FORMA #
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print(f)

# TERCEIRA FORMA USANDO O FOR. #
n = int(input('Digite um valor: '))
f = 1
for c in range(n, 0, -1):
    f = f * c
print(f'O fatorial de {n} é: {f}')
