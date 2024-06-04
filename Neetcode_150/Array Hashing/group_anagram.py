from string import ascii_lowercase
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        for i in strs:
            char_count = [0]*26
            key_str = ''
            for char in i:
                char_count[ascii_lowercase.index(char)] += 1
            count[tuple(char_count)].append(i)
        return list(count.values())
