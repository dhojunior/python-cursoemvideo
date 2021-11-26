print('-=-' * 12)
print('{:^36}'.format('DESAFIO 044'))
print('-=-' * 12)
valor = float(input('Digite o valor do produto: R$ '))
print('FORMAS DE PAGAMENTO')
print('1 - À vista em dinheiro ou cheque\n'
      '2 - À vista no cartão\n'
      '3 - 2x no cartão\n'
      '4 - 3x ou mais no cartão')
cond = int(input('Escolha a forma de pagamento através dos números acima: '))
if cond == 1:
    final = valor * 0.9
    print('Você vai receber 10% de desconto nessa condição, o valor será R$ {:.2f}'.format(final))
elif cond == 2:
    final = valor * 0.95
    print('Você vai receber 5% de desconto nessa condição, o valor será R$ {:.2f}'.format(final))
elif cond == 3:
    final = valor / 2
    print('Você deve pagar o valor integral em parcelas de R$ {:.2f}'.format(final))
elif cond == 4:
    parcela = int(input('Digite quantas parcelas quer pagar: '))
    final = valor / 0.8 / parcela
    print('Você vai pagar {} parcelas de R$ {:.2f}'.format(parcela, final))
else:
    print('Você não digitou uma opção de pagamento válida!')