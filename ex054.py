from datetime import date
print('-=-' * 12)
print('{:^36}'.format('DESAFIO 054'))
print('-=-' * 12)
maior = 0
menor = 0
anoatual = date.today().year
for c in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    if anoatual - nasc >= 18:
        maior += 1
    else:
        menor += 1
if menor == 0:
    print('Todas as pessoas são maiores de idade!')
elif menor == 1:
    print('6 pessoas são maiores de idade e 1 é menor!')
else:
    print('{} pessoas são maiores de idade e {} são menores!'.format(maior, menor))
