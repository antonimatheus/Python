import random
import time

print('-=' * 25)
print("Vou pensar em um número de 0 a 5. Tente advinhar...")
print('-=' * 25)

numeroEscolha = int(input('Qual o número que eu estou pensando? '))
numeroComputador = random.randint(0, 5)

if numeroEscolha > 5:
    print("ERRO! Digite números entre 0 e 5!")
else:
    print('PROCESSANDO...')
    time.sleep(2)

    if numeroEscolha > numeroComputador:
        print(f'PARABÈNS! Você conseguiu me vencer!')
    else:
        print(f'GANHEI! Pensei no {numeroComputador} não no {numeroEscolha}!')
