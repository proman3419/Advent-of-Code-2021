with open('5_i.txt') as f:
    A = f.read().splitlines()
    lines = []
    max_x = max_y = 0

    for e in A:
        d1, d2 = e.split(' -> ')
        x1, y1 = map(int, d1.split(','))
        x2, y2 = map(int, d2.split(','))

        if x1 > x2: x1, x2 = x2, x1
        if y1 > y2: y1, y2 = y2, y1

        if x1 == x2 or y1 == y2:
            if x2 > max_x: max_x = x2
            if y2 > max_y: max_y = y2
            lines.append((x1, y1, x2, y2))

M = [[0 for _ in range(max_x+1)] for _ in range(max_y+1)]

for l in lines:
    x1, y1, x2, y2 = l
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            M[y][x] += 1

print(sum(M[y][x] > 1 for y in range(max_y+1) for x in range(max_x+1)))
