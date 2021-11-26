print('-=-' * 12)
print('DESAFIO 042')
print('-=-' * 12)
print('VAMOS DESCOBRIR SE É POSSÍVEL FORMAR UM TRIÂNGULO?')
c1 = float(input('Digite o comprimento do primeiro lado: '))
c2 = float(input('Digite o comprimento do segundo lado: '))
c3 = float(input('Digite o comprimento do terceiro lado: '))
if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print('Com estes valores, é possível formar um triângulo!')
    if c1 == c2 == c3:
        print('E este triângulo será do tipo Equilátero!')
    elif c1 == c2 or c1 == c3 or c2 == c3:
        print('E este triângulo será do tipo Isósceles!')
    elif c1 != c2 != c3 != c1:
        print('E este triângulo será do tipo Escaleno!')
else:
    print('Com estes valores, não é possível formar um triângulo!')