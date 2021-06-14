def LookSay():
    a = '1'
    yield 1
    s = ''
    while True:
        k = 1
        for i in range(1,len(a)):
            if a[i] == a[i - 1]:
                k += 1
            else:
                s = s + str(k) + a[i - 1]
                yield k
                yield int(a[i - 1])
                k = 1
        s = s + str(k) + a[-1]
        yield k
        yield int(a[-1])
        a = s
        s = ''
    return s

#for i,l in enumerate(LookSay()):
#    print(f"{i}: {l}")
#    if i>10:
#        break

#print(list(zip(LookSay(),range(50501))))