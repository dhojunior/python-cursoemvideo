n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
lista = [n1, n2, n3]
print('O maior número digitado foi {}'.format(max(lista)))
print('O menor número digitado foi {}'.format(min(lista)))
# Correção Guanabara
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor número foi {}'.format(menor))
print('O maior número foi {}'.format(maior))