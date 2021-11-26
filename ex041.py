from datetime import date
print('-=' * 20)
print('DESAFIO 041')
print('-=' * 20)
nascimento = int(input('Digite o ano de nascimento do nadador: '))
idade = date.today().year - nascimento
print('COM {} ANOS'.format(idade))
print('A CATEGORIA DESTE NADADOR É: ')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
elif idade > 25:
    print('MASTER')
