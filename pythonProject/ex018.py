import math as m

valor = float(input('Digite o ângulo que você deseja: '))
rad = m.radians(valor)

sen = m.sin(rad)
cos = m.cos(rad)
tan = m.tan(rad)

print('-=' * 10)
print(f'O ângulo de {valor:.1f} tem o SENO de {sen:.2f}')
print(f'O ângulo de {valor:.1f} tem o COSSENO de {cos:.2f}')
print(f'O ângulo de {valor:.1f} tem o TANGENTE de {tan:.2f}')
print('-=' * 10)
