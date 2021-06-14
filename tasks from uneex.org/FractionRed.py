def nod(a,b):
    return nod(b, a%b) if b else a
a,b = eval(input())
x = a // b
p = nod(a - x * b, b)
y = (a - x * b) // p
z = b // p
if x != 0:
    print(x, end=' ')
if y != 0:
    print('{}/{}'.format(y,z))