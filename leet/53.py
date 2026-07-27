from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = [0]
        min_prefix = 0
        ans = nums[0]

        for i in nums:
            prefix.append(prefix[-1] + i)
            current = prefix[-1] - min_prefix
            ans = max(ans, current)
            min_prefix = min(min_prefix, prefix[-1])

        return ans
