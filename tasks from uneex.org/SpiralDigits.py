n,m = eval(input())
a = []
b = []
for i in range(m):
    for j in range(n):
        b.append(-1)
    a.append(b)
    b = []

state = [[0,1],[1,0],[0,-1],[-1,0]]
coord = [0,0]
k = 0
s = 0
f = 0
while f < (n * m):
    next = state[k]
    if (coord[0] + next[0] > m - 1):
        k = (k + 1) % 4
    elif (coord[1] + next[1] > n - 1):
        k = (k + 1) % 4
    elif (coord[1] + next[1] < 0):
        k = (k + 1) % 4
    elif (a[coord[0] + next[0]][coord[1] + next[1]] != -1):
        k = (k + 1) % 4
    next = state[k]

    a[coord[0]][coord[1]] = s
    coord[0] = coord[0] + next[0]
    coord[1] = coord[1] + next[1]
    s = (s + 1) % 10
    f += 1

#output
for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print()