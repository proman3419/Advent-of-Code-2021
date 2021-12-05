with open('5_i.txt') as f:
    A = f.read().splitlines()
    n = len(A)
    lines = [None]*n
    max_x = max_y = 0

    for i, e in enumerate(A):
        d1, d2 = e.split(' -> ')
        x1, y1 = map(int, d1.split(','))
        x2, y2 = map(int, d2.split(','))

        max_x = max(max_x, x1, x2)
        max_y = max(max_y, y1, y2)
        lines[i] = (x1, y1, x2, y2)

M = [[0 for _ in range(max_x+1)] for _ in range(max_y+1)]

for l in lines:
    x1, y1, x2, y2 = l

    if x1 == x2 or y1 == y2:                # vertical, horizontal
        if x1 > x2: x1, x2 = x2, x1
        if y1 > y2: y1, y2 = y2, y1

        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                M[y][x] += 1
    else:                                   # diagonal
        dx = -1 if x2 - x1 < 0 else 1
        dy = -1 if y2 - y1 < 0 else 1
        x = x1
        y = y1

        while x != x2 + dx and y != y2 + dy:
            M[y][x] += 1
            x += dx
            y += dy

print(sum(M[y][x] > 1 for y in range(max_y+1) for x in range(max_x+1)))
