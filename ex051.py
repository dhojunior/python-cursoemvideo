print('-=-' * 12)
print('{:^36}'.format('DESAFIO 051'))
print('-=-' * 12)
termo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
décimo = termo + (10 - 1) * razão
for c in range(termo, décimo + razão, razão):
    print(c)
