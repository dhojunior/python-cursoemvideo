import random
print('DESAFIO 019')
print('-' * 50)
aa = str(input('Digite o nome do primeiro aluno: '))
ab = str(input('Digite o nome do segundo aluno: '))
ac = str(input('Digite o nome do terceiro aluno: '))
ad = str(input('Digite o nome do quarto aluno: '))
#Ideal seria criar uma lista desta forma: lista = [aa, ab, ac, ad]
escolha = random.choice([aa, ab, ac, ad])
print('-' * 50)
print('O aluno escolhido para apagar o quadro foi: {}'.format(escolha))
print('-' * 50)
