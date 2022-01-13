"""
Faça um programa que leia nome e peso de várias pessoas,  guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

lista1 = list()
lista2 = list()
cont = maior = menor = 0
while True:
    lista1.append(str(input('Nome: ')))
    lista1.append(float(input('Peso: ')))
    if len(lista2) == 0:
        maior = menor = lista1[1]
    else:
        if lista1[1] > maior:
            maior = lista1[1]
        if lista1[1] < menor:
            menor = lista1[1]
    cont = cont + 1
    lista2.append(lista1[:])
    lista1.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Gostaria de continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
if cont == 1:
    print(f'Foram Cadastrada apenas {cont} Pessoa.')
else:
    print(f'Foram Cadastradas {cont} Pessoas.')
print(f'O maior peso foi de {maior} e pertence ah:', end='')
for c in lista2:
    if c[1] == maior:
        print(f'[{c[0]}] ', end='')
print(f'\nO menor peso foi de {menor} e pertence ah:', end='')
for c in lista2:
    if c[1] == menor:
        print(f'[{c[0]}] ', end='')

