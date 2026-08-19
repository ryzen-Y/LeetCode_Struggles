from typing import List

## BRUTE FORCE ##


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:

        seen = {}

        for i in range(len(nums) - k+1):
            window = set(nums[i:i+k])

            for i in window:
                seen[i] = seen.get(i, 0) + 1

        ans = - 1

        for i in seen:
            if seen[i] == 1:
                ans = max(ans, i)
        return ans
