from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        maximum = max(nums)
        minimum = min(nums)
        ans = []
        for i in range(minimum, maximum):
            if i not in nums:
                ans.append(i)
        return ans
