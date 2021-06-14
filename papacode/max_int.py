s = ''
while True:
    line = input()
    if len(line) == 0:
        break
    s += line.strip() + ' '

max = float('nan')

for token in s.split():
    try:
        num = int(token)
        if num > max or max != max:
            max = num
    except ValueError:
        continue

print(max)