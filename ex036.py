print('-=' * 20)
print('DESAFIO 036')
print('-=' * 20)
casa = float(input('Digite o valor do imóvel: R$ '))
sal = float(input('Digite o valor do salário: R$ '))
prazo = int(input('Quantos anos de financiamento: '))
parc = casa / (prazo * 12)
if parc > (sal * 0.3):
    print('\033[1;30;41mO valor da parcela R$ {:.2f} excede seu limite de faixa salarial que é de R$ {:.2f}\033[m'.format(parc, sal * 0.3))
else:
    print('\033[1;30;42mSeu limite foi aprovado, a parcela do seu financiamento será de R$ {:.2f} e deve ser paga por {} meses.\033[m'.format(parc, prazo * 12))