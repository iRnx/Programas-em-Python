"""
Crie um programa que tenha uma Tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa
deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""


tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
        'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
        'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    while num < 0 or num > 20:
        if num < 0 or num > 20:
            num = int(input('Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {tupla[num]}')
    resp = str(input('Gostaria de continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Gostaria de continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break


