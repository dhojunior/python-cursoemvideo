print('-=-' * 12)
print('{:^36}'.format('DESAFIO 048'))
print('-=-' * 12)
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print('Foram {} números que somam {}'.format(cont, s))
