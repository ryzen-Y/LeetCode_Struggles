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


# ========================= Optimized =======================

# class Solution:

    def findMiddleIndex(self, nums: List[int]) -> int:
        left_sum = [0]
        right = 0
        total = sum(nums)
        for i in nums:
            left_sum.append(left_sum[-1] + i)

        for i in range(len(nums)):
            right = total - left_sum[i] - nums[i]
            if right == left_sum[i]:
                return i
        return -1
