print('DESAFIO 06')
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1 / 2)
print('Você digitou {}: \nO dobro é {}. \nO triplo é {}. \nA raiz quadrada é {:.2f}.'.format(n, d, t, r))
# print('Você digitou {}: \nO dobro é {}. \nO triplo é {}. \nA raiz quadrada é {:.2f}.'.format(n, (n*2), (n*3), (n**(1/2))))
# Correção Guanabara - forma que usa menos memória
# Raiz quadrada dá pra fazer com pow = pow(n, (1/2))