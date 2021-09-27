"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
se o valor digitado for ímpar, desconsidere-o.
"""
soma = 0
cont = 0
for c in range(1, 7):
    n1 = int(input('Digite um número inteiro: '))
    if n1 % 2 == 0:
        soma = soma + n1
        cont = cont + 1
print(f'A soma dos pares é: {soma}')
print(f'Foram somados {cont} Números.')


