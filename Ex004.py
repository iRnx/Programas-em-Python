# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo#

a = input('Digite algo: ')
print(f'O tipo primitivo de \033[33m{a}\033[m é: {type(a)}')
print(f'É numerico?, {a.isnumeric()}')
print(f'É AlfaNumerico?, {a.isalnum()}')
print(f'É Alfa?, {a.isalpha()}')
print(f'É Maiúsculas?, {a.isupper()}')
print(f'É Minúsculas?, {a.islower()}')
print(f'Está Capitalizada?, {a.istitle()}')
print(f'Só tem espaços?, {a.isspace()}')
print(f'É número da tabela ASCII?, {a.isascii()} ')
