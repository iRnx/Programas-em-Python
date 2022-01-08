"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta
de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""

lista = list()
for c in range(0, 5):
    n = int(input("Digite o numero: "))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        for i, v in enumerate(lista):
            if n <= v:
                lista.insert(i, n)
                print(f'Adicionado na posição {i} da lista...')
                break
print(lista)



