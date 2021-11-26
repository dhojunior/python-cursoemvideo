import random
import time
print('-=-' * 12)
print('DESAFIO 045')
print('-=-' * 12)
print('VAMOS JOGAR PEDRA, PAPEL E TESOURA?')
lista = ['PEDRA', 'PAPEL', 'TESOURA']
print('As opções são:\n'
      '1 - PEDRA\n'
      '2 - PAPEL\n'
      '3 - TESOURA')
escolha = int(input('Escolha uma das três opções: '))
if escolha == 1:
    jogador = 'PEDRA'
elif escolha == 2:
    jogador = 'PAPEL'
elif escolha == 3:
    jogador = 'TESOURA'
else:
    print('Você não escolheu uma opção válida, jogue novamente!')
    quit()
computador = random.choice(lista)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
print('-=-' * 15)
print('Você escolheu {}'.format(jogador))
print('Eu escolhi {}'.format(computador))
print('-=-' * 15)
if jogador == computador:
    print('EMPATAMOS!')
elif jogador == 'PEDRA' and computador == 'TESOURA':
    print('Pedra é mais forte que tesoura\n'
          'VOCÊ GANHOU!!')
elif jogador == 'PEDRA' and computador == 'PAPEL':
    print('Papel é mais forte que Pedra\n'
          'VOCÊ PERDEU!!')
elif jogador == 'PAPEL' and computador == 'PEDRA':
    print('Papel é mais forte que pedra\n'
          'VOCÊ GANHOU!!')
elif jogador == 'PAPEL' and computador == 'TESOURA':
    print('Tesoura é mais forte que papel\n'
          'VOCÊ PERDEU!!')
elif jogador == 'TESOURA' and computador == 'PAPEL':
    print('Tesoura é mais forte que papel\n'
          'VOCÊ GANHOU!!')
elif jogador == 'TESOURA' and computador == 'PEDRA':
    print('Pedra é mais forte que tesoura\n'
          'VOCÊ PERDEU!!')
