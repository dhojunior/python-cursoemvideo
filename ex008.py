print('DESAFIO 08')
m = float(input('Escreva a medida em metros: '))
cm = m * 100
mm = m * 1000
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
#print('{}m é igual a {:.0f}cm e {:.0f}mm'.format(m, cm, mm))
print('A medida {:.2f}m corresponde a: \n{:.2f} km \n{:.2f} hm \n{:.2f} dam \n{:.2f} dm \n{:.2f} cm \n{:.2f} mm'.format(m, km, hm, dam, dm, cm, mm))
