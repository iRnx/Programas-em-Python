"""
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a
expressão passada está com os parênteses abertos e fechados na ordem correta.
"""

expr = str(input('Digite a expressão: ')).strip().upper()
if expr == '':
    print('VOCÊ NÃO DIGITOU NADA')
    exit()
pilha = []
for s in expr:
    if s == '(':
        pilha.append('(')
    elif s == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua Expressão esta correta')
else:
    print('Sua Expressão esta errada')


