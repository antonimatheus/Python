'''num = int(input('Informe um número: '))

print(f'Analizando o número {num}.')

mil = (num / 1000)
num %= 1000

cent = (num / 100)
num %= 100

dez = (num / 10)
num %= 10

uni = num

print('-_' * 10)
print(f'Unidade: {uni:.0f}')
print(f'Dezena: {dez:2.0f}')
print(f'Centena: {cent:.0f}')
print(f'Milhar: {mil:2.0f}')
print('-_' * 10)'''

num = int(input('Informe um número: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Analizando o número {num}.')

print('-_' * 10)
print(f'Unidade: {u}')
print(f'Dezena: {d:2}')
print(f'Centena: {c}')
print(f'Milhar: {m:2}')
print('-_' * 10)
