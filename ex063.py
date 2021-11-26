n = int(input('Digite quantos elementos quer ver da sequência de Fibonacci: '))
c = 1
f = 0
a = 0
s = 0
while c <= n:
    if f == 0:
        print(0)
        s = f
        f += 1
        c += 1
    else:
        print(f)
        a = f + s
        f = f + a
        c += 1
