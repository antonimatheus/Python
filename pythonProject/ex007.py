print('*Digite suas notas para saber sua média.')

nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
nota3 = int(input('Digite a terceira nota: '))

med = (nota1 + nota2 + nota3) / 3

print(f' A média das notas {nota1}, {nota2} e {nota3} é igual a {med:.2f}')

if med < 7:
    print('Você está reprovado!')
elif med == 7:
    print('Você está na média!')
else:
    print('PARABÉNS! Você está acima da média!')
