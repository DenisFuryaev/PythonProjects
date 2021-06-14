n = eval(input())
f = False
while (n > 1) and not(f):
    f = True
    for i in range(2,n):
        f = (n % i != 0) * f
    n -= 1
print(n + 1)