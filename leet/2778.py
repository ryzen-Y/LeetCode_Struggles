class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:

        add = 0

        n = len(nums)
        for i in range(1, n + 1):
            if n % i == 0:
                add += (nums[i - 1] * nums[i - 1])
        return add
