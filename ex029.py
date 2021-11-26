# Desafio 029
vel = float(input('Digite a velocidade que você costuma dirigir na rodovia: '))
if vel > 80:
    print('\033[1;30;41mVOCÊ FOI MULTADO:\033[m')
    print('Você excedeu o limite da via que é de 80 km/h')
    print('O valor da multa é de R$ 7.00 a cada km/h acima do permitido')
    print('Andando a {} km/h a multa é de R${:.2f}'.format(vel, (vel - 80) * 7))
else: #Poderia não ser utilizado
    print('\033[1;30;42mParabéns, você é um motorista prudente e não será multado!\033[m') #Poderia não ser utilizado
print('Dirija com segurança')