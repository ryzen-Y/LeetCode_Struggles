from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor = 0
        has_nonzero = False

        for i in nums:
            xor ^= i
            if i != 0:
                has_nonzero = True

        if xor != 0:
            return len(nums)
        return len(nums) - 1 if has_nonzero else 0
