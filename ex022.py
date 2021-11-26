print('-' * 50)
print('DESAFIO 021')
print('-' * 50)
# Ler o nome completo de uma pessoa e mostrar:
# O nome com todas as letras maiusculas
# O nome com todas minúsculas
# Quantas letras ao todo sem contar espaços
# Quantas letras tem o primeiro nome
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em minúsculas é {}.'.format(nome.lower()))
print('Seu nome contém {} letras'.format(len(nome.replace(' ', ''))))#pode ser len(nome) - nome.count(' ')
dividido = nome.split()
print('Seu primeiro nome {}, contém {} letras'.format(dividido[0], len(dividido[0])))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
#Correção Guanabara