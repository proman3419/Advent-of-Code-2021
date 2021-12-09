def is_low_point(B, x, y):
    flag = True

    if 0 <= y-1 and B[y-1][x] <= B[y][x]: flag = False
    if y+1 < n and B[y+1][x] <= B[y][x]: flag = False
    if 0 <= x-1 and B[y][x-1] <= B[y][x]: flag = False
    if x+1 < m and B[y][x+1] <= B[y][x]: flag = False

    return flag


with open('9_i.txt') as f:
    A = f.read().splitlines()
    n = len(A)
    m = len(A[0])
    B = [[int(A[y][x]) for x in range(m)] for y in range(n)]

_sum = 0
for y in range(n):
    for x in range(m):
        if is_low_point(B, x, y):
            _sum += B[y][x] + 1

print(_sum)
