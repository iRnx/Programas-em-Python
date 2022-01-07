"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.
"""

v1 = list()
while True:
    v2 = int(input('Digite os valores: '))
    if v2 not in v1:
        v1.append(v2)
        print('\033[32mValor adicionado com Sucesso\033[m')
    else:
        print('\033[31mValor Duplicado, não foi inserido na lista.\033[m')
    resp = str(input('Gostaria de continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        print('Entrada inválida.Digite novamente!')
        resp = str(input('Gostaria de continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
v1.sort()
print(f'Os valores Digitados foram: {v1}')

