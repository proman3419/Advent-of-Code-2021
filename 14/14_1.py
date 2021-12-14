from collections import Counter


with open('14_i.txt') as f:
    A = f.read().splitlines()
    template = A[0]
    rules = {}

    for i in range(2, len(A)):
        k, v = A[i].split(' -> ')
        rules[k] = v

polymer = list(template)
steps = 10

for s in range(steps):
    i = 0
    while i + 1 < len(polymer):
        k = polymer[i] + polymer[i+1]
        if k in rules:
            polymer.insert(i+1, rules[k])
            i += 2
        else:
            i += 1

occ = Counter(polymer)
occ_sorted = [occ[k] for k in sorted(list(occ), key=lambda x: occ[x])]

print(occ_sorted[-1] - occ_sorted[0])
