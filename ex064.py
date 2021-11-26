s = 0
o = 0
c = 1
n = ''
while n != 999:
    n = int(input('Digite o {}º número: '.format(c)))
    if n != 999:
        c += 1
        s += n
    else:
        print('Obrigado por usar o programa!')
print('A soma dos {} números digitados é {}.'.format(c - 1, s))