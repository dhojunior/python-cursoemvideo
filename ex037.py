print('-=' * 20)
print('DESAFIO 037')
print('-=' * 20)
num = int(input('Digite o número que quer converter: '))
print('Escolha a conversão abaixo')
print('[1] BINÁRIO')
print('[2] OCTAL')
print('[3] HEXADECIMAL')
escolha = int(input('Digite a opção: '))
if escolha == 1:
    print('{} convertido pra BINÁRIO é {}.'.format(num, bin(num)[2:])) '''[2:] lê apenas da segunda posição pra frente'''
elif escolha == 2:
    print('{} convertido para OCTAL é {}.'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('{} convertido para HEXADECIMAL é {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')
