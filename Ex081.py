"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

v1 = list()
cont = 0
while True:
    v2 = int(input('Digite os numeros que quer adicionar na lista: '))
    cont = cont + 1
    v1.append(v2)
    resp = str(input('Gostaria de continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        print(f'\033[31mEntrada inválida.Digiti novamente\033[m')
        resp = str(input('Gostaria de continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('=-=-=' * 12)
v1.sort(reverse=True)
print(f'Foram digitados {cont} números.')
print(f'Forma decrescente: {v1}')
if 5 in v1:
    print(f'O número 5 esta na lista.')
else:
    print('O numero 5 não esta na lista.')


