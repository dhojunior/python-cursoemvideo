print('DESAFIO 05')
n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print('O número {} é precedido por {} e sucedido por {}'.format(n, a, s))

# Correção do Guanabara - Dessa forma ocupa menos memória:
print('Sem variáveis')
print('O número {} é precedido por {} e sucedido por {}'.format(n, (n-1), (n+1)))