with open('2_i.txt') as f:
    A = f.readlines()

x = depth = aim = 0
for e in A:
    cmd, X = e.split()
    X = int(X)

    if cmd == 'forward': 
        x += X
        depth += aim * X
    elif cmd == 'down': aim += X
    elif cmd == 'up': aim -= X

print(x*depth)
