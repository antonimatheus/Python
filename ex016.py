from math import trunc
print('*Coloque um valor quebrado para transformarmos ele em um inteiro.')

value = float(input('Digite um valor: '))
newValue = trunc(value)

print(f'O valor de {value} passou a ser agora o inteiro {newValue}!')
