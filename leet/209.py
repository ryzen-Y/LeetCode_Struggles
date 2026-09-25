class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        add = 0
        minimum = float('inf')

        for right in range(len(nums)):
            add += nums[right]
            if add >= target:
                while add >= target:
                    minimum = min(minimum, right - left + 1)
                    add -= nums[left]
                    left += 1

        if minimum == float('inf'):
            return 0
        else:
            return minimum
