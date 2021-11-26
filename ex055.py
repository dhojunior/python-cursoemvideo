print('-=-' * 12)
print('{:^36}'.format('DESAFIO 055'))
print('-=-' * 12)
maior = 0
menor = 1000
for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O maior peso foi {}kg e o menor foi {}kg!'.format(maior, menor))
