import math
#Poderia importar de forma from math import trunc
print('-' * 50)
print('DESAFIO 016')
print('-' * 50)
num = float(input('Digite um número real: '))
inteiro = math.trunc(num)
#trunc(num)
#Sem importação int(num)
print('O número {} tem {} como a parte inteira'.format(num, inteiro))
