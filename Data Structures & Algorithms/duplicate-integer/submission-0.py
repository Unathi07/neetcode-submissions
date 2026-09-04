class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = {}
        for num in nums:
            dup[num] = dup.get(num, 0) + 1
        return any(count > 1 for count in dup.values())
            

        