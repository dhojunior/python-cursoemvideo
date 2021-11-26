# Desafio 031
dist = float(input('Qual a distância da Viagem: '))
print('Vou calcular o valor da viagem de {} km para você.'.format(dist))
if dist <= 200:
    print('O Valor cobrado será de R${:.2f}.'.format(dist * 0.50))
else:
    print('O valor cobrado será de R${:.2f}.'.format(dist * 0.45))
print('BOA VIAGEM')
# preço = dist * 0.50 if dist <= 200 else dist * 0.45
