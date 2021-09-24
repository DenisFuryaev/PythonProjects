import math

if __name__ == "__main__":
    k = int(input())
    result = -1

    for b in range(2, 10000000):
        a = b
        b = b * k;
        digits_a = int(math.log10(a)) + 1
        digits_b = int(math.log10(b)) + 1
        if digits_a == digits_b:
            a_last_digit = a % 10
            a_saved = a
            a = a // 10
            if (a_last_digit * 10**(digits_a - 1) + a) == b:
                result = a_saved
                break

    print(result)