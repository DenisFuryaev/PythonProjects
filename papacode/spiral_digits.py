m, n = eval(input())

t = []
for i in range(n):
    t.append([])
    for j in range(m):
        t[i].append('*')

def update_direction(x, y, d, maxX, maxY):
    if d == 1:
        if x+1 >= maxX or t[y][x+1] != '*':
            d = 2
        else:
            return d
    if d == 2:
        if y+1 >= maxY or t[y+1][x] != '*':
            d = 3
        else:
            return d
    if d == 3:
        if x-1 < 0 or t[y][x-1] != '*':
            d = 4
        else:
            return d
    if d == 4:
        if y-1 < 0 or t[y-1][x] != '*':
            d = 1
        else:
            return d
    if d == 1:
        if x+1 >= maxX or t[y][x+1] != '*':
            return 0
    return 1

dir = 1
c = 0
x, y = 0, 0

while dir != 0:
    t[y][x] = str(c)
    dir = update_direction(x, y, dir, m, n)
    if dir == 1:
        x += 1
    elif dir == 2:
        y += 1
    elif dir == 3:
        x -= 1
    elif dir == 4:
        y -= 1
    c = (c + 1) % 10

for i in t:
    print(' '.join(i))