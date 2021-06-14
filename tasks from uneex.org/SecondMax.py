s = eval(input())
max1 = s[0]
min = s[0]
for i in s:
    if i > max1:
        max1 = i
    if i < min:
        min = i
max2 = min
for i in s:
    if (i > max2) and (i != max1):
        max2 = i
if min == max1:
    print('NO')
else: print(max2)