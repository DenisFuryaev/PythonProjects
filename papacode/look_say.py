def LookSay():
    s = [1]
    yield s[0]

    s_prev, s_next = [1], []

    while True:
        digit = 0
        count = 0

        for c in s_prev:
            if count == 0:
                digit = c
                count = 1
                continue

            if c == digit:
                count += 1
                continue

            yield count
            s_next.append(count)
            yield digit
            s_next.append(digit)

            digit = c
            count = 1

        if count != 0:
            yield count
            s_next.append(count)
            yield int(digit)
            s_next.append(digit)

        s_prev = s_next
        s_next = []
        s.append(s_prev)

for i,l in enumerate(LookSay()):
    print(f"{i}: {l}")
    if i>10:
        break