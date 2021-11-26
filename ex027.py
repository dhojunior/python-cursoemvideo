# Nome completo - retorna primeiro e último nome
nome = str(input('Digite seu nome completo: ')).title().strip()
separado = nome.split()
print('Olá {}, seja bem vindo(a)!'.format(nome))
print('Seu primeiro nome é {}.'.format(separado[0]))
print('Seu último nome é {}.'.format(separado[len(separado) - 1]))
