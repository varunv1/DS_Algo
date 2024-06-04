def valid_anagram(t, s):
    from collections import defaultdict
    if len(i) != len(s):
        return False
    d = defaultdict(d)
    for i in t:
        d[i] += 1
    for i in s:
        d[i] -= 1
    for i in d.values():
        if i != 0:
            return False
    return True
