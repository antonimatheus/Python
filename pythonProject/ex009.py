"""
print('De qual número você gostaria de saber da tabuada?')
tab = int(input('número: '))

print(f'{tab} x 0 = {tab * 0}')
print(f'{tab} x 1 = {tab * 1}')
print(f'{tab} x 2 = {tab * 2}')
print(f'{tab} x 4 = {tab * 4}')
print(f'{tab} x 5 = {tab * 5}')
print(f'{tab} x 6 = {tab * 6}')
print(f'{tab} x 7 = {tab * 7}')
print(f'{tab} x 8 = {tab * 8}')
print(f'{tab} x 9 = {tab * 9}')
print(f'{tab} x 10 = {tab * 10}')
"""

print('De qual número gostaria de saber da tabuada? E até quanto?')
tabuada = int(input('tabuada: '))
limite = int(input('até: '))

for i in range(1, limite + 1):
    print(f'{tabuada} x {i:2} = {tabuada*i}')
