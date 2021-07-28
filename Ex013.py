# Faça um algoritmo que leia o sálario de um funcionário e mostre seu novo salário, com 15% de aumento. #

salario = float(input('Qual é o salário do Funcionário? R$'))
aumento = salario + (salario * 15 / 100)
print(f'Um funcionário que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${aumento:.2f}')
