print('-' * 50)
print('DESAFIO 023')
print('-' * 50)
#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
'''num = str(input('Digite um número de 0 a 9999: '))
qtd = len(num)
print('Unidade: {}'.format(num[qtd-1]))
print('Dezena: {}'.format(num[qtd-2]))
print('Centena: {}'.format(num[qtd-3]))
print('Milhar: {}'.format(num[qtd-qtd]))'''
#Correção Guanabara
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
#DIFÍCIL DEMAIS!!!!!!!