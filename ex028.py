import random
import time

print('-=' * 10)
print("Vou pensar em um número de 0 a 5. Tente advinhar...")
print('-=' * 10)

numeroEscolha = int(input('Qual o número que eu estou pensando? '))
numeroComputador = random.randint(0, 5)

if numeroEscolha > 5:
    print("ERRO! Digite números entre 0 e 5!")
else:
    print('PROCESSANDO...')
    time.sleep(2)

    if numeroEscolha > numeroComputador:
        print(f'PARABÈNS, você conseguiu me vencer!')
    else:
        print(f'GANHEI! Você errou o número que eu pensei!')

    print(f'Número que pensei: {numeroComputador}, número dado: {numeroEscolha}.')