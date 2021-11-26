import math
#Poderia importar dessa forma: from math import hypot
print('-' * 50)
print('DESAFIO 017')
print('-' * 50)
ca = float(input('Digite o tamanho do cateto adjascente: '))
co = float(input('Digite o tamanho do cateto oposto: '))
h = math.hypot(ca, co)
print('Num triângulo retângulo de lados {} e {}, a hipotenusa terá medida {:.2f}'.format(ca, co, h))
#Poderia ser da seguinte forma: hip = (co ** 2 + ca ** 2) ** (1/2)
