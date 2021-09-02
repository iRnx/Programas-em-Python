"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome
separadamente.
Exemplo: ana maria de souza
primeiro: ana
último: souza
"""

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro Nome é: {nome[0]}')
print(f'Seu último nome é: {nome[len(nome) - 1]}')
