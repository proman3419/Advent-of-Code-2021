from collections import defaultdict


with open('14_i.txt') as f:
    A = f.read().splitlines()
    template = A[0]
    rules = {}

    for i in range(2, len(A)):
        k, v = A[i].split(' -> ')
        rules[k] = v

polymer = defaultdict(int)
for i in range(len(template)-1):
    polymer[template[i]+template[i+1]] += 1
steps = 40

for s in range(steps):
    curr = defaultdict(int)

    keys = list(polymer.keys())
    for k in keys:
        curr[k[0]+rules[k]] += polymer[k]
        curr[rules[k]+k[1]] += polymer[k]

    polymer = curr

polymer[template[-1]+' '] = 1

occ = defaultdict(int)
for k in polymer:
    occ[k[0]] += polymer[k]

occ_sorted = [occ[k] for k in sorted(list(occ), key=lambda x: occ[x])]

print(occ_sorted[-1] - occ_sorted[0])
