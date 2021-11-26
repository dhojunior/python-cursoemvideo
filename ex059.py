n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
opção = ''
resultado = ''
while opção != 5:
    print('-*-' * 12)
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] digitar novos números
[5] sair do programa''')
    opção = int(input('Escolha uma das opções acima: '))
    if opção == 1:
        resultado = n1 + n2
        print('\033[32mSoma: {} + {} = {}\033[m'.format(n1, n2, resultado))
    elif opção == 2:
        resultado = n1 * n2
        print('\033[32mMultiplicação: {} x {} = {}\033[m'.format(n1, n2, resultado))
    elif opção == 3:
        resultado = max(n1, n2)
        print('\033[32mO maior número entre {} e {}, é {}\033[m'.format(n1, n2, resultado))
    elif opção == 4:
        n1 = int(input('Digite o novo 1º Número: '))
        n2 = int(input('Digite o novo 2º Número: '))
    elif opção == 5:
        print('\033[32mObrigado por usar nosso programa!\033[m')
    else:
        print('\033[31mVocê digitou uma opção inválida! Tente novamente\033[m')
