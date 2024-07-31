salario = float(input('Qual o seu salário atual? R$'))

if salario > 1250:
    acrescimo = (10/100) * salario
    res = salario + acrescimo
else:
    acrescimo = (15/100) * salario
    res = salario + acrescimo
    """
        res = salario + ((15/100) * salario) <--- simplificado
    """

print(f'O seu salário passou de R${salario:.2f} para R${res:.2f} agora.')
