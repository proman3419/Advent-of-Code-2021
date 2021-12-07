from math import floor, ceil


def calculate_cost(crabs, median):
    return sum(abs(c-median) for c in crabs)


with open('7_i.txt') as f:
    crabs = list(map(int, f.read().split(',')))

crabs.sort()
n = len(crabs)

if n % 2 == 1:
    median = crabs[n//2]
    print(calculate_cost(crabs, median))
else:
    median1 = floor((crabs[n//2-1] + crabs[n//2]) / 2)
    median2 = ceil((crabs[n//2-1] + crabs[n//2]) / 2)
    print(min(calculate_cost(crabs, median1),
              calculate_cost(crabs, median2)))
