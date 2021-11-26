from datetime import date
print('-=' * 20)
print('DESAFIO 039')
print('-=' * 20)
print('''Qual seu gênero:
[1] Feminino
[2] Masculino''')
sexo = int(input('Escolha a opção conforme a lista acima: '))
if sexo == 1:
    print('Você não precisa se alistar. Obrigado por usar o programa!')
    quit()
elif sexo != 1 and sexo != 2:
    print('Você digitou uma opção inválida, tente novamente.')
    quit()
else:
    print('Você é homem e tem o alistamento obrigatório!')
nasc = int(input('Digite o seu ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você deve se alistar este ano!')
elif idade < 18:
    print('Você ainda vai se alistar, e isso será daqui a {} ano(s) em {}.'.format(18 - idade, atual + (18 - idade)))
else:
    print('Você já se alistou, e isso foi há {} ano(s) em {}.'.format(idade - 18, atual - (idade - 18)))
