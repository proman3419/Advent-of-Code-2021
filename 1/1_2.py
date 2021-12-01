with open('1_2i.txt') as f:
    A = list(map(int, f.readlines()))

n = len(A)
_sum = 0
for i in range(n-3):
    three_meas = sum(A[i+j] for j in range(3))
    if three_meas < three_meas - A[i] + A[i+3]:
        _sum += 1        

print(_sum)
