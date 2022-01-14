"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""

lista1 = [[], []]

for c in range(1, 7 + 1):
    valor = int(input(f'Digite o {c} valor: '))
    if valor % 2 == 0:
        lista1[0].append(valor)
    if valor % 2 == 1:
        lista1[1].append(valor)
lista1[0].sort()
lista1[1].sort()
print(f'Valores Pares: {lista1[0]}')
print(f'Valores Ímpares: {lista1[1]}')

