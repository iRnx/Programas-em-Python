"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
valor digitado e as suas respectivas posições na lista.
"""

maior = menor = 0
lista1 = list()
for c in range(0, 5):
    lista2 = int(input(f'Digite um valor na posição {c}: '))
    lista1.append(lista2)
    if c == 0:
        maior = menor = lista1[c]
    else:
        if lista1[c] > maior:
            maior = lista1[c]
        if lista1[c] < menor:
            menor = lista1[c]
print('=-=' * 15)
print(f'Os valores digitados são: {lista1}')
print(f'O Maior valor digitado é: {maior} nas posições ', end='')
for i, v in enumerate(lista1):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nE o Menor valor digitado é: {menor} nas posições', end='')
for i, v in enumerate(lista1):
    if v == menor:
        print(f' {i}...', end='')




