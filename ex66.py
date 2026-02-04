# DESAFIO 66
count = 0
sum = 0
while True:
    num = int(input('Type the number [999 to stop]: '))
    if num == 999:
        break
    count += 1
    sum += num
print(f"You've typed {count} numbers and the sum is {sum}")