class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums) - 1
        seen = {}

        for i in nums:
            seen[i] = seen.get(i, 0) + 1
            if seen[i] > n // 2:
                return i
