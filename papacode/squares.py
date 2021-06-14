def squares(h, w, *args):
    a = []
    for i in range(h):
        b = []
        for j in range(w):
            b.append('.')
        a.append(b)

    for arg in args:
        for i in range(arg[2]):
            for j in range(arg[2]):
                a[i + arg[1]][j + arg[0]] = arg[3]

    for x in range(len(a)):
        print(''.join(a[x]))

#squares(20,23,(1,1,5,'@'), (2,3,1,'!'), (4,5,11,'#'), (8,11,9,'/'))