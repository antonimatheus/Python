from math import sqrt, pow

catetoAdjacente = float(input('Digite o valor do cateto adjacente: '))
catetoOposto = float(input('Digite o valor do cateto oposto: '))
hipotenusa = (pow(catetoAdjacente, 2)) + (pow(catetoOposto, 2))
res = sqrt(hipotenusa)

print('-=' * 20)
print(f'Com o Cateto Adjacente valendo {catetoAdjacente}')
print(f'Com o Cateto Oposto valendo {catetoAdjacente}')
print(f'O valor da hipotenusa será de {res:.2f}')
print('-=' * 20)
