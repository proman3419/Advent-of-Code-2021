with open('1_i.txt') as f:
    A = list(map(int, f.readlines()))

print(sum(A[i] < A[i+1] for i in range(len(A)-1)))
