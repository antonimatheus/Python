aluguel = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))

aluguelPagar = aluguel * 60
kmPagar = km * 0.15
res = aluguelPagar + kmPagar

print('-_' * 15)
print(f'O total a pagar é de R${res:.2f}')
print('-_' * 15)
