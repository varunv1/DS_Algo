def bitStr(n, s):
    if n == 1:
        return s
    return [digit+bit for digit in bitStr(1, s) for bit in bitStr(n-1, s)]


print(bitStr(3, 'abc'))
