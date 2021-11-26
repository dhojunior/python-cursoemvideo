print('-=-' * 12)
print('{:^36}'.format('DESAFIO 062'))
print('-=-' * 12)
print('{:^36}'.format('GERADOR DE PA'))
print('-=-' * 12)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
termo = primeiro
mais = 10
total = 0
cont = 1
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer apresentar? '))
print('Finalizado com a apresentação de {} termos!'.format(total))
