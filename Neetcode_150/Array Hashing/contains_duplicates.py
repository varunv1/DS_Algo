from collections import defaultdict


class Solution:
    def containsDuplicate(self, nums):
        count_store = defaultdict(int)
        for i in nums:
            if count_store[i]+1 > 1:
                return True
            count_store[i] += 1
        return False
