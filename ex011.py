print('DESAFIO 011')
larg = float(input('Largura da parede em metros: '))
alt = float(input('Altura da parede em metros: '))
m2 = larg * alt
tinta = m2 / 2
latas = tinta / 3.6
print('-' * 50)
print('A área da parede é {:.2f}m². \nPara pintá-la você precisará de {:.2f}L de tinta, \nO que equivale a {:.1f} latas de '
      '3.6L'.format(m2, tinta, latas))
print('-' * 50)
