with open('6_i.txt') as f:
    fish = list(map(int, f.read().split(',')))

states_cnt = 9
FSC = [0]*states_cnt
for f in fish:
    FSC[f] += 1

for d in range(256):
    children = FSC[0]
    _FSC = [FSC[i+1] if i+1 < states_cnt else 0 for i in range(states_cnt)]
    _FSC[6] += children
    _FSC[8] += children
    FSC = _FSC

print(sum(FSC))
