num = float(input('Qual a distância da sua viagem? '))

if num <= 200:
    viagemCurta = num * 0.50
    print(f'A distância de {num:.1f}km lhe custará R${viagemCurta:.2f}.')
else:
    viagemLonga = num * 0.45
    print(f'A distância de {num:.1f}km lhe custará R${viagemLonga:.2f}.')