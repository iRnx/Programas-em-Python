"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a
digitar valores.
"""

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma = soma + num
    quant = quant + 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
media = soma / quant
print(f'Você digitou {quant} números e a média foi: {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
