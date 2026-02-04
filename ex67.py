#DESAFIO 67 - TABUADA
num = 0
tab = 0
while True:
    num = int(input('Type the number [Negative to stop]: '))
    if num <= 0:
        break
    print(f"Showing the multiplication table of {num}")
    for i in (range(1, 11)):
        tab = num * i
        print(f'{num} x {i} = {tab}')
print(f"You've finished printing the multiplication table")