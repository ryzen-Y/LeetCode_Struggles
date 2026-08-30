from typing import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        maximum = max(nums)
        minimum = min(nums)

        index_miximum = nums.index(maximum)
        index_minimim = nums.index(minimum)

        left = min(index_miximum, index_minimim)
        right = max(index_miximum, index_minimim)
        n = len(nums)

        from_left = right + 1
        from_right = n - left
        from_both_side = (left + 1) + (n - right)

        return min(from_left, from_right, from_both_side)
