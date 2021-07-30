"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
lendo o nome deles e escrevendo o nome do escolhido.
"""

import random
primeiro = str(input('Pimeiro Aluno: '))
segundo = str(input('Segundo Aluno: '))
terceiro = str(input('Terceiro Aluno: '))
quarto = str(input('Quarto Aluno: '))
lista = [primeiro, segundo, terceiro, quarto]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')
