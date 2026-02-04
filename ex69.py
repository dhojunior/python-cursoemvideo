#DESAFIO 69
funder = over = m = f = count = 0
while True:
    age = int(input('Enter the age: '))
    gender = input('Enter the gender [M/F]: ').upper().strip()[0]
    if age >= 18:
        over += 1
    if gender == 'M':
        m += 1
    elif gender == 'F':
        f+= 1
        if age < 20:
            funder += 1
    dec = str(input("Would you like to continue? [Y/N]: ")).upper().strip()[0]
    if dec == 'N':
        break
print(f'There are {over} people over 18 years old, {m} men in total and {funder} women under 20 years old')