#DESAFIO 71 - CAIXA ELETRONICO
valor = int(input('Digite o valor para saque R$: '))
cinc = valor // 50
troco = valor % 50
vint = troco // 20
troco = troco % 20
dez = troco // 10
troco = troco % 10
um = troco // 1
print(f'{cinc} Notas de R$ 50,00')
print(f'{vint} Notas de R$ 20,00')
print(f'{dez} Notas de R$ 10,00')
print(f'{um} Notas de R$ 1,00')
