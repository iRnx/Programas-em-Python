"""
Crie um programa que faça o computador jogar JOKENPÔ com você.
"""

from random import randint
from time import sleep
computador = randint(0, 2)
itens = ('pedra', 'papel', 'tesoura')
print('''Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a jogada?  '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 15)
print(f'COMPUTADOR JOGOU: {itens[computador]}')
print(f'JOGADOR JOGOU: {itens[jogador]}')
print('-=' * 15)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR WIN')
    elif jogador == 2:
        print('COMPUTADOR WIN')

if computador == 1:
    if jogador == 0:
        print('COMPUTADOR WIN')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR WIN')

if computador == 2:
    if jogador == 0:
        print('JOGADOR WIN')
    elif jogador == 1:
        print('COMPUTADOR WIN')
    elif jogador == 2:
        print('EMPATE')
