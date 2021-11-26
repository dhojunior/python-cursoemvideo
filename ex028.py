# Desafio 028
import random
import time
print('-*-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente Adivinhar...')
print('-*-' * 20)
print('')
chute = int(input('Qual número eu escolhi: '))
# num = random.choice([0, 1, 2, 3, 4, 5])
num = random.randint(0, 5) # Faz o computador sortear
print('')
print('PROCESSANDO...')
print('')
time.sleep(3)
print('O número que eu escolhi foi {}!'.format(num))
if chute == num:
    print('PARABÉNS, você acertou!!!')
else:
    print('QUE PENA, tente novamente!')
