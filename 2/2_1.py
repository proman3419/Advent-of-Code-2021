with open('2_i.txt') as f:
    A = f.readlines()

x = depth = 0
for e in A:
    cmd, X = e.split()
    X = int(X)

    if cmd == 'forward': x += X
    elif cmd == 'down': depth += X
    elif cmd == 'up': depth -= X

print(x*depth)
