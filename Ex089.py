"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

lista1 = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    lista1.append([nome, [nota1, nota2], media])
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Gostaria de continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(lista1):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    escolha = int(input('Digite o numero do aluno (digite 999 para interromper): '))
    if escolha == 999:
        print('****finalizado****')
        break
    for i, k in enumerate(lista1):
        if i == escolha:
            print(f'notas de {lista1[i][0]} foi {lista1[i][1]}')


