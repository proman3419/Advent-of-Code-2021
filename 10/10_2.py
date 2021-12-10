op = set(['(', '[', '{', '<'])
op_to_cl = {'(': ')', '[': ']', '{': '}', '<': '>'}
cl_to_val = {')': 1, ']': 2, '}': 3, '>': 4}


def get_line_error_val(l):
    stack = []

    for ch in l:
        if ch in op:
            stack.append(ch)
        else:
            if op_to_cl[stack.pop()] != ch:
                return -1

    error_val = 0
    for ch in stack[::-1]:
        error_val = error_val*5 + cl_to_val[op_to_cl[ch]]

    return error_val


with open('10_i.txt') as f:
    A = f.read().splitlines()

error_vals = []
for l in A:
    error_val = get_line_error_val(l)
    if error_val != -1:
        error_vals.append(error_val)

print(sorted(error_vals)[len(error_vals)//2])
