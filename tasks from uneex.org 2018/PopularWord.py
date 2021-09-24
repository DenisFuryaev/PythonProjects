def dic(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

s = input()

a = ''
while s != '':
    a = a + s.strip() + ' '
    s = input()

h = dic(a.split())
max = 0
maxi = ''
for i in h:
    b = h.get(i,0)
    if b > max:
        max = b
        maxi = i
k = 0
for i in h:
    b = h.get(i,0)
    if b == max:
        k = k + 1
if k > 1:
    print('---')
else: print(maxi)