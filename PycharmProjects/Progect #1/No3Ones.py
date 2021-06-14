n = eval(input())
k = 0
for i in range(2**n):
    b = i
    while b != 0:
        b  = b >> 1
print(k)