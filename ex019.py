from random import choice

v1 = str(input('Primeiro aluno: '))
v2 = str(input('Segundo aluno: '))
v3 = str(input('Terceiro aluno: '))
v4 = str(input('Quarto aluno: '))
students = [v1, v2, v3, v4]
res = choice(students)

print(f'O aluno escolhido foi {res}!')
