print('Adicione o salário e a % do aumento!')

salario = float(input('Salário: '))
aumento = int(input('% do aumento do salário: '))

salarioAumento = (aumento / 100) * salario
novoPreco = salario + salarioAumento

print(f'O salário de R${salario:.2f} e {aumento:.0f}% de aumento, o salário atual será de R${novoPreco:.2f}!')
