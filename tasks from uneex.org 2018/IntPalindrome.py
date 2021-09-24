def pal(a):
    check = (a % 10) == (a // 10**(len(str(a)) - 1))
    if len(str(a)) <= 1:
        return True
    a = a - (a // 10**(len(str(a)) - 1))*(10**(len(str(a)) - 1))
    a = a//10
    return pal(a) and check
if pal(eval(input())):
    print('YES')
else: print('NO')