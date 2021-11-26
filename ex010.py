print('DESAFIO 010')
real = float(input('Digite quantos reais você possui: R$ '))
dolar = real / 5.34
euro = real / 6.47
print('-' * 30)
print('COMPRA DO DIA COM R$ {:.2f}'.format(real))
print('-' * 30)
print('')
print('Euro: {:.2f} €'.format(euro))
print('Dólar: US$ {:.2f}'.format(dolar))
