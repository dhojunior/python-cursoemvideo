r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
'''list = [r1, r2, r3]
list.sort()
if (list[2] - list[1]) < list[0] < (list[2] + list[1]):
    if (list[2] - list[0]) < list[1] < (list[2] + list[0]):
        if (list[1] - list[0]) < list[2] < (list[1] + list[0]):
            print('Com os valores {}, {} e {} é possível formar um triângulo'.format(r1, r2, r3))
else:
    print('Com os valores {}, {} e {} não é possível formar um triângulo.'.format(r1, r2, r3))'''
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[30;42mOs segmentos {}, {} e {} PODEM FORMAR um triângulo\033[m'.format(r1, r2, r3))
else:
    print('\033[30;41mOs segmentos {}, {} e {} NÃO PODEM FORMAR um triângulo\033[m'.format(r1, r2, r3))
