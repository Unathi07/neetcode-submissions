from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        sorted_keys = sorted(counts.keys(), key=counts.get,reverse=True)

        return sorted_keys[:k]

        