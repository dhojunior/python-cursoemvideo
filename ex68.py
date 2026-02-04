#DESAFIO 68 - PAR OU ÍMPAR
import random
wins = 0
while True:
    dec = str(input("ODD or EVEN [O/E]: ")).upper().split()[0]
    num = int(input('Type the number: '))
    pcnum = random.randint(0,10)
    sum = num + pcnum
    if sum % 2 == 0:
        if dec == 'E':
            print(f'The sum is {sum}, an even number: You WON')
            wins += 1
        elif dec == 'O':
            print(f'The sum is {sum}, an even number: You LOST')
            break
    elif sum % 2 != 0:
        if dec == 'O':
            print(f'The sum is {sum}, an odd number: You WON')
            wins += 1
        elif dec == 'E':
            print(f'The sum is {sum}, an odd number: You LOST')
            break
print(f"Game Over! You've won {wins} times.")