def first(_iter):
    return list(_iter)[0]


def translate_and_sum(inv_chars_map, to_sum):
    digits = [[1, 1, 1, 0, 1, 1, 1],
              [0, 0, 1, 0, 0, 1, 0],
              [1, 0, 1, 1, 1, 0, 1],
              [1, 0, 1, 1, 0, 1, 1],
              [0, 1, 1, 1, 0, 1, 0],
              [1, 1, 0, 1, 0, 1, 1],
              [1, 1, 0, 1, 1, 1, 1],
              [1, 0, 1, 0, 0, 1, 0],
              [1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 0, 1, 1]]        

    res = 0
    for signal in to_sum:
        digit = [0]*7
        for ch in signal:
            digit[ord(inv_chars_map[ch])-ord('a')] = 1
            
        digit_val = first(i for i in range(10) 
                          if all(digit[j] == digits[i][j] for j in range(7)))
        res = 10*res + digit_val

    return res


def solve(signals, to_sum):
    all_letters = 'abcdefg'
    dts = [None]*10 # digit to set
    chars_map = {ch: '' for ch in all_letters}

    for signal in signals:
        if len(signal) == 2: dts[1] = signal
        elif len(signal) == 3: dts[7] = signal
        elif len(signal) == 4: dts[4] = signal
        elif len(signal) == 7: dts[8] = signal

    dts[9] = first(filter(lambda x: len(dts[4] & x) == 4 \
                                 and len(x) == 6, signals))
    dts[0] = first(filter(lambda x: len(dts[1] & x) == 2 \
                                 and len(x) == 6 \
                                 and x != dts[9], signals))
    dts[6] = first(filter(lambda x: len(x) == 6 \
                                 and x not in (dts[0], dts[9]), signals))

    chars_map['a'] = first(dts[7] - dts[1])
    chars_map['e'] = first(dts[8] - dts[9])
    chars_map['c'] = first(dts[8] - dts[6])
    chars_map['d'] = first(dts[8] - dts[0])
    chars_map['b'] = first(dts[4] - (dts[1] | set(chars_map['d'])))
    chars_map['g'] = first(dts[9] - (dts[4] | (set(chars_map['a']))))
    chars_map['f'] = first(set(all_letters) - set(chars_map.values()))

    inv_chars_map = {v: k for k, v in chars_map.items()}

    return translate_and_sum(inv_chars_map, to_sum)


with open('8_i.txt') as f:
    A = f.read().splitlines()

_sum = 0
for l in A:
    signals, to_sum = l.split('|')
    signals = list(map(set, signals.strip().split()))
    to_sum = to_sum.split()
    _sum += solve(signals, to_sum)

print(_sum)
