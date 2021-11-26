print('-=-' * 12)
print('{:^36}'.format('DESAFIO 056'))
print('-=-' * 12)
soma = 0
velhonome = ''
velhoidade = 0
mulheres = 0
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma += idade
    if sexo == 'M':
        if velhoidade == 0:
            velhonome = nome
            velhoidade = idade
        elif idade > velhoidade:
            velhoidade = idade
            velhonome = nome
    elif sexo == 'F':
        if idade < 20:
            mulheres += 1
print('A média de idade das 4 pessoas é {}'.format(soma/4))
print('O homem mais velho é {} e ele tem {} anos.'.format(velhonome, velhoidade))
print('Tem {} mulheres menores de 20 anos.'.format(mulheres))
