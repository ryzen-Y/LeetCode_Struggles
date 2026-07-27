from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix_sum = [0]
        right_sum = [0] * len(nums)
        total = sum(nums)

        for i in nums:
            prefix_sum.append(prefix_sum[-1] + i)

        for i in range(len(nums)):
            right_sum[i] = total - prefix_sum[i] - nums[i]
            if right_sum[i] == prefix_sum[i]:
                return i
        return -1
