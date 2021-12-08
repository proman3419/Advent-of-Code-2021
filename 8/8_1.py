with open('8_i.txt') as f:
    A = f.read().splitlines()

n = len(A)
permitted_lens = set([2, 3, 4, 7])

cnt = 0
for l in A:
    for signal in l.split('|')[1].split():
        if len(signal) in permitted_lens:
            cnt += 1

print(cnt)
