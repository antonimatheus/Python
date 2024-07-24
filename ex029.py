velocidade = float(input('Qual a velocidade atual do carro: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você ultrapassou a velocidade permitida! Sua multa é de R${multa:.2f}.')
else:
    print('Você está andando na velocidade permitida! Boa viagem!')