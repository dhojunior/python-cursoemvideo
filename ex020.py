from random import shuffle
print('DESAFIO 020')
print('-' * 50)
aa = str(input('Digite o nome do primeiro aluno: '))
ab = str(input('Digite o nome do segundo aluno: '))
ac = str(input('Digite o nome do terceiro aluno: '))
ad = str(input('Digite o nome do quarto aluno: '))
alunos = [aa, ab, ac, ad] #Essa é a lista que eu já havia criado "sem querer"
shuffle(alunos) #Não usa variável
print('A ordem de apresentação será: ')
print(alunos)
