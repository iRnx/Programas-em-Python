"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, Calcule seu IMC e mostre seu status, de acordo com
a tabela abaixo:
- Abaixo de 18.5: ABAIXO DO PESO
- Entre 18.5 e 25: PESO IDEAL
- 25 até 30: SOBREPESO
- 30 ATÉ 40: OBESIDADE
- Ácima de 40: OBESIDADE MÓRBIDA
"""

peso = float(input('Qual é seu peso? (kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.2f}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, CUIDADO !')

