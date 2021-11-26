#Nome da cidade e dizer se começa ou não com a palavra 'Santo'
cidade = str(input('Digite o nome da sua cidade: ')).strip()
div = cidade.lower().split()
print('santo' in div[0])
#Correção Guanabara
print(cidade[:5].upper() == 'SANTO')