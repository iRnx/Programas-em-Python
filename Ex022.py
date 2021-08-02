"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
-> O nome com todas  as letras maiúsculas e minúsculas.
-> Quantas letras ao todo (sem considerar os espaços).
-> Quantas letras tem o primeiro nome.
"""

nome = str(input('Qual seu nome inteiro? ')).strip()
print(f'Seu nome em Maiúsculo é: {nome.upper()}')
print(f'Seu nome em Minúsculo é: {nome.lower()} ')
print(f'Seu nome tem {len(nome) - nome.count(" ")} letras')
print(f'seu primeiro nome tem {nome.find(" ")} letras')

