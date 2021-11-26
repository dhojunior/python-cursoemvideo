print('-=-' * 12)
print('{:^36}'.format('DESAFIO 057'))
print('-=-' * 12)
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos, informe seu sexo [M/F]: ')).strip().upper()[0]
print('Opção correta, você digitou a opção {}!'.format(sexo))
