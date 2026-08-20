from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        prev_sum = 0

        for x in range(k):
            prev_sum += nums[x]

        max_sum = prev_sum

        i = 1
        j = k

        while j < len(nums):
            prev_sum = prev_sum + nums[j] - nums[i - 1]

            if prev_sum > max_sum:
                max_sum = prev_sum

            i += 1
            j += 1

        return max_sum / k
