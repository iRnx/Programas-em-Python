"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter
apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final,
mostre o conteúdo das três listas geradas.
"""

lista = list()
listapar = list()
listaimpar = list()
while True:
    v1 = int(input('Digite os numeros: '))
    lista.append(v1)
    if v1 % 2 == 0:
        listapar.append(v1)
    elif v1 % 2 == 1:
        listaimpar.append(v1)
    resp = str(input('Gostaria de continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        print('Entrada inválida.Tente novamente.')
        resp = str(input('Gostaria de continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {listapar}')
print(f'A lista de ímpares é: {listaimpar}')
