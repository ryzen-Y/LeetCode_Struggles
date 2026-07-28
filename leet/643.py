from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        prefix_sum = [0]

        for i in nums:
            prefix_sum.append(prefix_sum[-1] + i)

        max_sum = float('-inf')

        for i in range(k, len(prefix_sum)):
            current = prefix_sum[i] - prefix_sum[i - k]
            max_sum = max(max_sum, current)

        return max_sum / k
