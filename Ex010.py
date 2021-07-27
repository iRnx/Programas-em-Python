# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre Quantos Dólares ela pode comprar #

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.17
print(f'Com R${real} você pode comprar US${dolar:.2f}')
