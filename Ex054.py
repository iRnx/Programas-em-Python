"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores.
"""

from datetime import date
atual = date.today().year
contmaior = 0
contmenor = 0
for c in range(1, 8):
    nasc = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        contmaior = contmaior + 1
    else:
        contmenor = contmenor + 1
print(f'Ao todo tivemos {contmaior} pessoas de idade')
print(f'E também tivemos {contmenor} pessoas menores de idade')
