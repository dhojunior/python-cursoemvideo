from random import randint
from time import sleep
print('''Vamos jogar um jogo?
Vou pensar num número de 0 a 10 e você tem que adivinhar qual número eu pensei!''')
print('Deixa eu ver', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('\nPronto, já pensei no meu número!')
computador = randint(0, 10)
palpites = 0
opção = ''
while opção != computador:
    opção = int(input('Me diga o seu chute: '))
    palpites += 1
    if opção < computador:
        print('É mais, tente novamente!')
    elif opção > computador:
        print('É menos, tente novamente!')
print('Parabéns, você acertou e só precisou de {} tentativa(s)!!!'.format(palpites))
