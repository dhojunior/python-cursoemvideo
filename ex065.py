n = 0
c = 1
o = 'S'
soma = 0
while o == 'S':
    n = int(input('Digite o {}º número: '.format(c)))
    soma += n
    c += 1
    o = str(input('Quer continuar [S/N]: ')).upper()
print('A soma dos valores foi: {}'.format(soma))