"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

n1 = (int(input('Digite um número: ')),
      int(input('Digite outro número: ')),
      int(input('Digite mais número: ')),
      int(input('Digite o último número: ')))
print(f'Você digitou os valores: {n1}')
print(f'O valor 9 apareceu {n1.count(9)} vezes')
if 3 in n1:
    print(f'O valor 3 apareceu na {n1.index(3) + 1} posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for c in n1:
    if c % 2 == 0:
        print(c, end='')




