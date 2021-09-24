"""
Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço FOR.
"""
n1 = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{n1} x {c} = ', n1 * c)
