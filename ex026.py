#Leia uma frase e diga quantas vezes aparece:
#Quantas Letra A
#Em que posição aparece a primeira vez
#Em que posição aparece a última vez
frase = str(input('Digite uma frase: ')).lower().strip()
print('A Letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('A primeira Letra A aparece na posição {}.'.format(frase.find('a') + 1))
print('A última letra A aparece na posição {}.'.format(frase.rfind('a') + 1))