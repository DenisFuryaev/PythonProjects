def fun(a , b):
    print(locals())
    c = 8
    print(locals())
    return b, a
fun(1, 2)
