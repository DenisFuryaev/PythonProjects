def moar(a,b,n):
    x = 0
    y = 0
    for i in a:
        if i % n == 0: x += 1
    for i in b:
        if i % n == 0: y += 1
    if x > y:
        return True
    else: return False