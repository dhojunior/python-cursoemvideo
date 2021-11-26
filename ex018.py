import math
print('DESAFIO 018')
print('-' * 50)
an = float(input('Digite o ângulo: '))
#Deve ser em radianos
angulo = math.radians(an)
sen = math.sin(angulo)
cos = math.cos(angulo)
tan = math.tan(angulo)
print('Para o ângulo {}, temos os seguintes valores: \nSeno: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f}'.format(an, sen, cos, tan))
