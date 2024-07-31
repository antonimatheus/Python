p = float(input('Primeiro número: '))
s = float(input('Segundo número: '))
t = float(input('Terceiro número: '))

res = [p, s, t]

maior = max(res)
menor = min(res)

print(f'O maior número é {maior:.2f} e o menor número é {menor:.2f}')
