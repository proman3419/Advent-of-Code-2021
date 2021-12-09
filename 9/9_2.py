from math import prod


directions_4 = [          (0, -1), 
                (-1,  0),          (1,  0),
                          (0,  1)         ]


def is_low_point(B, x, y):
    flag = True

    if 0 <= y-1 and B[y-1][x] <= B[y][x]: flag = False
    if y+1 < n and B[y+1][x] <= B[y][x]: flag = False
    if 0 <= x-1 and B[y][x-1] <= B[y][x]: flag = False
    if x+1 < m and B[y][x+1] <= B[y][x]: flag = False

    return flag


def field_needs_check(x, y, visited, basins_map, B, n, m):
    if x < 0 or x >= m or y < 0 or y >= n: return False
    if B[y][x] >= 9: return False
    if visited[y][x] == 1 or basins_map[y][x] != -1: return False

    return True


def find_max_basins_areas(B, n, m, low_points):
    def rec(x, y, prev_h):
        nonlocal B, n, m, visited, basins_map, basin_id, area

        if B[y][x] > prev_h:
            visited[y][x] = 1
            basins_map[y][x] = basin_id
            area += 1

            for d in directions_4:
                _x = x + d[0]
                _y = y + d[1]
                if field_needs_check(_x, _y, visited, basins_map, B, n, m):
                    rec(_x, _y, B[y][x])

    basins_map = [[-1 for _ in range(m)] for _ in range(n)]
    basin_id = 0

    max_basins_areas = [-1, -1, -1]

    for low_point in low_points:
        x, y = low_point
        visited = [[0 for _ in range(m)] for _ in range(n)]
        area = 0
        rec(x, y, -1)

        basin_id += 1

        max_basins_areas.append(area)
        max_basins_areas.remove(min(max_basins_areas))

    return max_basins_areas


with open('9_i.txt') as f:
    A = f.read().splitlines()
    n = len(A)
    m = len(A[0])
    B = [[int(A[y][x]) for x in range(m)] for y in range(n)]

low_points = [(x, y) for x in range(m) for y in range(n) 
                if is_low_point(B, x, y)]

max_basins_areas = find_max_basins_areas(B, n, m, low_points)
print(prod(max_basins_areas))
