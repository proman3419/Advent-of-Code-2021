with open('3_i.txt') as f:
    A = f.read().splitlines()

N = len(A)
n = len(A[0])
balance = [0 for _ in range(n)]

for i in range(N):
    for j in range(n):
        if A[i][j] == '0': balance[j] -= 1
        elif A[i][j] == '1': balance[j] += 1

gamma = sum(2**(n-1-i) for i in range(n) if balance[i] > 0)
epsilon = 2**n - 1 - gamma

print(gamma * epsilon)
