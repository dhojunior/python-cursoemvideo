x = 1
y = 1
z = 0
count = int(input("Enter the quantity of Fibonacci's number you want to know: "))
i = 1
while i <= count:
    # if i == 1:
    #     print(z)
    #     i += 1
    #     x = y
    #     y = z
    #     z = x + y
    # # elif i == 2:
    # #     print(y)
    # #     i += 1
    # else:
    print('{} --> '.format(z), end='')
    x = y
    y = z
    z = z + x
    # print("X = {x}, Y = {y}, Z = {z}".format(x=x, y=y, z=z))
    i += 1
print('END')