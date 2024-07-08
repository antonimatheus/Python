altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

area = altura * largura
tinta = area / 2

print(f'A parede de altura {altura:.2f}m e largura {largura:.2f}m, possui a área de {area:.2f}m².')
print(f'Sabendo que o litro de tinta pinta 2m², precisaria de {tinta:.2f} litros de tinta!')
