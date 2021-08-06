# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'. #

cidade = str(input('Em que cidade vc nasceu? ')).strip()
print(f'{cidade[:5].upper() == "SANTO"}')
