"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
números gerados e também indique o menor e o maior valor que estão na tupla.
"""

# PRIMEIRA FORMA #
from random import sample
tupla = sample(range(1, 10,), 5)
ordenada = sorted(tupla)
print(tupla)
print(f'O maior numero é: {ordenada[4]} e o menor é: {ordenada[0]}')

# SEGUNDA FORMA #
from random import sample
tupla = sample(range(1, 10,), 5)
print(tupla)
print(f'O maior numero é: {max(tupla)} e o menor é: {min(tupla)}')
