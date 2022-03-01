"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""

dicio = dict()
lista1 = list()
cont = conts = contm = 0
while True:
    dicio.clear()
    dicio['nome'] = str(input('Nome: '))
    cont = cont + 1
    dicio['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while dicio["sexo"] not in 'MF':
        if dicio["sexo"] not in 'MF':
            print('\033[31mERRO! Responda apenas M ou F.\033[m')
            dicio['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    dicio['idade'] = int(input('Idade: '))
    conts = conts + dicio['idade']
    contm = conts / cont
    lista1.append(dicio.copy())
    resp = str(input('Gostaria de continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        print('\033[31mERRO! Responda apenas S ou N.\033[m')
        resp = str(input('Gostaria de continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'A) Foram cadastradas {cont} pessoas.')
print(f'B) A Média das pessoas é de: {contm:.2f} anos de idade.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in lista1:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=', ')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in lista1:
    if p['idade'] >= contm:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<<ENCERRADO>>>')

