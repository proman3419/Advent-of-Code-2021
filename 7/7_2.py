with open('7_i.txt') as f:
    crabs = list(map(int, f.read().split(',')))

crabs.sort()
n = len(crabs)
_min = min(crabs)
_max = max(crabs)

move_costs = [(0+i)/2 * (i+1) for i in range(_max+1)]

min_cost = float('inf')
for align_pos in range(_min, _max+1):
    curr_cost = 0
    for c in crabs:
        curr_cost += move_costs[abs(c-align_pos)]

    min_cost = min(min_cost, curr_cost)

print(int(min_cost))
