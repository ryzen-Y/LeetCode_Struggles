from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        n = len(nums)
        ans = []

        for i in range(n):
            prefix.append(prefix[-1] * nums[i])
            suffix.append(suffix[-1] * nums[n - 1 - i])
        suffix.reverse()

        for i in range(n):
            ans.append(prefix[i] * suffix[i+1])

        return ans
