"""
Crie um programa que leia dois valores e mostre um menu como o ao lado na tela:
Seu programa deverá realizar a operação solicitada em cada caso.
[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA
"""
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
escolha = 0
maior = 0
while escolha != 5:
    print("""====================
    [ 1 ] SOMA
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA
    
=====================""")
    escolha = int(input('Escolha um número do menu: '))
    while escolha > 5 or escolha < 1:
        if escolha > 5 or escolha < 1:
            print('Entrada inválida.Digite novamente')
            escolha = int(input('Escolha um número do menu: '))

    if escolha == 1:
        soma = n1 + n2
        print(f'Sua soma é: {n1} + {n2} = {soma}')
    if escolha == 2:
        mult = n1 * n2
        print(f'Sua Multiplicação é: {n1} * {n2} = {mult}')
    if escolha == 3:
        if n1 > n2:
            maior = n1
        if n2 > n1:
            maior = n2
        print(f'entre {n1} e {n2} o maior é {maior}')
    if escolha == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    if escolha == 5:
        print('FIM DO PROGRAMA! VOLTE SEMPRE!')



