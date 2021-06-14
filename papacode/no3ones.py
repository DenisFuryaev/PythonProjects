n = eval(input())

if n == 3:
    print('1')
    exit()

ones = [0, 0, 1]
#alls = [2, 4, 8]
for i in range(3, n):
    ones.append(2**(i-2) + ones[i-1] + ones[i-2] + ones[i-3])
#    alls.append(2**(i+1))

#for i in range(n):
#    print(i, ' : ', alls[i], '-', ones[i], ' = ', alls[i] - ones[i])

print(2**(n) - ones[n-1])
