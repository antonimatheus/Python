name = str(input('Digite o seu nome completo: ')).strip()

caps = name.upper()
minus = name.lower()
quant = len(name) - name.count(' ')
pName = name.split()
quantPName = len(pName[0])

print(f'O seu nome em MAIÚSCULA É {caps}')
print(f'O seu nome em minúscula é {minus}')
print(f'O seu nome tem ao todo {quant} letras')
print(f'O seu primeiro nome {pName[0]} tem {quantPName} letras')
