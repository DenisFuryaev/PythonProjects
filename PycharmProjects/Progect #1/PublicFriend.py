a = eval(input())
d = dict()
while a != (0,0):

    if a[0] not in d:
        d[a[0]] = str(a[1])
    else: d[a[0]] = d[a[0]] + str(a[1])

    if a[1] not in d:
        d[a[1]] = str(a[0])
    else: d[a[1]] = d[a[1]] + str(a[0])

    a = eval(input())
print(d)