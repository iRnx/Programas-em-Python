"""
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando
o total de vitórias consecutivas que ele conquistou no final do jogo.
"""

from random import randint
soma = par = impar = cont = 0
while True:
    print('=-=' * 12)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('=-=' * 12)
    computador = randint(0, 10)
    n = int(input('Diga um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    while escolha not in 'PI':
        print('Entrada inválida.Tente novamente.')
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('=-=' * 12)
    soma = n + computador
    print(f'Você jogou {n} e o computador {computador} e o total deu {soma} ')
    print('=-=' * 12)
    if escolha == 'P':
        if soma % 2 == 0:
            print('VOCÊ GANHOU DEU PAR ')
            cont = cont + 1
        else:
            print('VOCÊ PERDEU DEU ÍMPAR')
            break
    if escolha == 'I':
        if soma % 2 == 1:
            print('VOCÊ GANHOU DEU ÍMPAR')
            cont = cont + 1
        else:
            print('VOCÊ PERDEU DEU PAR')
            break
print(f'VOCE VENCEU {cont} vezes')