# link https://leetcode.com/problems/determine-if-string-halves-are-alike/description/?envType=daily-question&envId=2024-01-12
from collections import Counter
def halvesAreAlike( s: str) -> bool:
    new_len = int(len(s)/2)
    s, t = s[0:new_len], s[new_len:]
    s = Counter(s.lower())
    t = Counter(t.lower())
    vovels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for key, value in s.items():
        if key in vovels:
            count += value
    for key, value in t.items():
        if key in vovels:
            count -= value
    return True if count == 0 else False

if __name__ == "__main__":
    s = "textbook"
    print(halvesAreAlike(s))