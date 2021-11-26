sal = float(input('Digite o salário do funcionário: R$ '))
if sal > 1250:
    print('De acordo com a tabela de aumento, o salário de R$ {:.2f} receberá um aumento de \033[1;36m10%'.format(sal))
    print('O novo salário será de R$ {:.2f}.'.format(sal * 1.1))
else:
    print('De acordo com a tabela de aumento, o salário de R$ {:.2f} receberá um aumento de \033[;136m15%.'.format(sal))
    print('O novo salário será de R$ {:.2f}.'.format(sal * 1.15))
