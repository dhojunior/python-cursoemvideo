print('-' * 50)
print('DESAFIO 015')
dias = int(input('Digite a quantidade de dias de locação: '))
km = float(input('Digite a quantidade de km utilizados: '))
diaria = dias * 60
dist = km * 0.15
print('-' * 50)
print('Você locou o carro por {} dias e rodou {:.2f} km, abaixo está a tabela de valores:'.format(dias, km))
print('Valor da Locação: R$ 60.00\nValor por km rodado: R$ 0.15\nValor Diárias: R$ {:.2f}\nValor distância: R${:.2f}\nValor Total: R$ {:.2f}'.format(diaria, dist, diaria + dist))
print('-' * 50)
pago = (dias * 60) + (km * 0.15)
print('Valor total a pagar é R$ {:.2f}'.format(pago))
