def generator(n):
    yield -n
    yield str(n)
    yield (abs(n) // 10) % 10