#DESAFIO 70 - NOME E PREÇO
sum = overt = count = 0
cheap = 0
cheapname = ""
while True:
    name = str(input("What is the product name? "))
    price = float(input("What is the price of the product? "))
    sum += price
    if price > 1000:
        overt += 1
    if count == 0:
        cheap = price
        cheapname = name
    else:
        if price < cheap:
            cheap = price
            cheapname = name
    count += 1

    dec = str(input("Do you want to continue? [Y/N] ")).upper().strip()[0]
    if dec == 'N':
        break

print(f'The total spent is {sum:.2f}, {overt} cost more than 1000 and the cheapest product is {cheapname}')
