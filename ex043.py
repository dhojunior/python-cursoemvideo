print('-=-' * 12)
print('DESAFIO 043')
print('-=-' * 12)
peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em m: '))
imc = peso / (altura ** 2)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO IDEAL!')
elif imc < 25:
    print('Você está dentro do PESO IDEAL!')
elif imc < 30:
    print('Você está com SOBREPESO!')
elif imc <= 40:
    print('Você está com OBESIDADE!')
elif imc > 40:
    print('Você está com OBESIDADE MÓRBIDA')
