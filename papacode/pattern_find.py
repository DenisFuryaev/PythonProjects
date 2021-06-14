import re

s = input()
p = input()

pattern = p.replace('@', ".")
match = re.search(pattern, s)

if match:
    print(match.start(0))
else:
    print('-1')

