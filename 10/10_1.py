op = set(['(', '[', '{', '<'])
op_to_cl = {'(': ')', '[': ']', '{': '}', '<': '>'}
cl_to_val = {')': 3, ']': 57, '}': 1197, '>': 25137}


def get_line_error_val(l):
    stack = []

    for ch in l:
        if ch in op:
            stack.append(ch)
        else:
            if op_to_cl[stack.pop()] != ch:
                return cl_to_val[ch]

    return 0


with open('10_i.txt') as f:
    A = f.read().splitlines()

_sum = 0
for l in A:
    _sum += get_line_error_val(l)

print(_sum)
