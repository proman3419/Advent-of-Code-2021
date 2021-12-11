directions_8 = [(-1, -1), (0, -1), (1, -1),
                (-1,  0),          (1,  0),
                (-1,  1), (0,  1), (1,  1)]


def solve(B, flashed, n, m):
    def rec(x, y):        
        nonlocal B, flashed, flashed_cnt, n, m

        if x < 0 or x >= m or y < 0 or y >= n:
            return

        B[y][x] += 1

        if flashed[y][x] == 0 and B[y][x] > 9:
            flashed[y][x] = 1
            flashed_cnt += 1
            B[y][x] = 0

            for d in directions_8:
                rec(x+d[0], y+d[1])

    flashed_cnt = 0

    for y in range(n):
        for x in range(m):
            rec(x, y)

    for y in range(n):
        for x in range(m):
            if flashed[y][x] == 1:
                B[y][x] = 0
                flashed[y][x] = 0

    return flashed_cnt


with open('11_i.txt') as f:
    A = f.read().splitlines()
    n = len(A)
    B = [None]*n

    for i, l in enumerate(A):
        B[i] = [int(ch) for ch in l]

m = len(B[0])
flashed = [[0 for _ in range(m)] for _ in range(n)]
steps = 100

_sum = 0
for s in range(steps):
    _sum += solve(B, flashed, n, m)

print(_sum)
