# Algo
# Instead of matching pattern with each chr, we just match
# the hashed value

def robin_karp(text=None, pattern=None):
    if text == '' or text == None:
        return -1
    if pattern == '' or pattern == None:
        return -1
    if len(pattern) > len(text):
        return -1
    hash_p = hash(pattern)
    start = 0
    end = len(pattern) - 1
    while start <= end and start + len(pattern)
