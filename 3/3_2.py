def filter_bins(A, N, n, balance, filter_func):
    i = 0
    eliminated = 0
    _A = [1]*N
    _balance = [balance[i] for i in range(n)]

    while N - eliminated > 1:
        for j in range(N):
            if _A[j] != 0 and filter_func(A[j][i], i, _balance):
                _A[j] = 0
                eliminated += 1
                for k in range(i+1, n):
                    _balance[k] += 1 if A[j][k] == '0' else -1
        i += 1

    for i in range(N):
        if _A[i] == 1:
            return A[i]


with open('3_i.txt') as f:
    A = f.read().splitlines()

N = len(A)
n = len(A[0])
balance = [0 for _ in range(n)]

for i in range(N):
    for j in range(n):
        if A[i][j] == '0': balance[j] -= 1
        elif A[i][j] == '1': balance[j] += 1

OGR = int(filter_bins(A, N, n, balance, 
                  lambda x, i, B: x == '0' if B[i] == 0 else \
                  not (x == '1' and B[i] > 0 or x == '0' and B[i] < 0)), 2)
CO2SR = int(filter_bins(A, N, n, balance, 
                    lambda x, i, B: x == '1' if B[i] == 0 else \
                    (x == '1' and B[i] > 0 or x == '0' and B[i] < 0)), 2)

print(OGR * CO2SR)
