"""
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

from random import shuffle
primeiro = str(input('Pimeiro Aluno: '))
segundo = str(input('Segundo Aluno: '))
terceiro = str(input('Terceiro Aluno: '))
quarto = str(input('Quarto Aluno: '))
lista = [primeiro, segundo, terceiro, quarto]
shuffle(lista)
print(f'A ordem de apresentação será:\n{lista}')
