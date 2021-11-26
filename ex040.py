print('-=' * 20)
print('DESAFIO 040')
print('-=' * 20)
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
if n1 > 10 or n2 > 10:
    print('Você digitou uma nota inválida. Digite uma nota entre 0 e 1')
    quit()
elif n1 < 0 or n2 < 0:
    print('Você digitou uma nota inválida. Digite uma nota entre 0 e 1')
    quit()
media = (n1 + n2) / 2
print('Sua média foi {:.1f}'.format(media))
if media < 5:
    print('Você está \033[1;30;41mREPROVADO!\033[m')
    print('Nos vemos novamente no próximo ano!')
elif 5 <= media < 7:
    print('Você está de \033[1;30;43mRECUPERAÇÃO.\033[m')
    print('Prepare-se bem para a prova!')
elif media >= 7:
    print('Parabéns, você está \033[1;30;42mAPROVADO!!!\033[m')
