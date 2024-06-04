from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        bucket_array = [[] for i in range(len(nums)+1)]
        for key, value in d.items():
            bucket_array[value].append(key)
        output = []
        # print(bucket_array)
        for items in bucket_array[-1::-1]:
            # print(items, 'item')
            if items != [] and len(output) < k:
                output.extend(items)
        return output[:k]
