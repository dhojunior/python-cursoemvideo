print('-=-' * 12)
print('{:^36}'.format('DESAFIO 053'))
print('-=-' * 12)
frase = str(input('Digite uma frase: ')).strip().upper().replace(' ','')
'''palavras = frase.split()
junto = ''.join(palavras)
print(junto)
inverso = '' # Tirando o for pode-se usar inverso = junto[::-1]
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(inverso)
if junto == inverso:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')'''
print(frase)
inverso = frase[::-1]
print(inverso)
if frase == inverso:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')