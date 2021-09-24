def fun(x,y,r):
    a,b = eval(input())
    if (a == b == 0):
            return True
    value = (x - a)**2 + (y - b)**2 <= r**2
    return fun(x,y,r) and value
x,y,r = eval(input())
f = fun(x,y,r)
if f:
    print('YES')
else: print('NO')