# find all rectangles in input matrix

# ------------
# .###.....#..
# .###.##..#..
# .....##.....
# .....##..#..
# ............
# ............
# .####..####.
# .......####.
# .......####.
# ------------

# 6


result = 0
prev_rects = []


def parse(str):
    prev_char = "."
    rect = [0, 0]
    curr_rects = []
    global prev_rects
    global result

    for idx, char in enumerate(str):
        if char == "#" and prev_char == ".":
            rect[0] = idx
        else:
            if char == "." and prev_char == "#":
                rect[1] = idx - 1
                curr_rects.append([rect[0], rect[1]])
        prev_char = char

    for prev_rect in prev_rects:
        if prev_rect not in curr_rects:
            result += 1
    prev_rects = curr_rects


if __name__ == "__main__":
    str = input()
    new_str = input()
    while new_str != str:
        parse(new_str)
        new_str = input()

    for rect in prev_rects:
        result += 1

    print(result)

