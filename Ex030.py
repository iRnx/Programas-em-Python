# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR. #

n = int(input('Digite um numero: '))
if n % 2 == 0:
    print(f'O número {n} é par')
elif n % 2 == 1:
    print(f'O número {n} é ímpar')
