class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:

        total = sum(nums)
        target = total - x

        if target < 0:
            return -1

        left = 0
        current_sum = 0
        maximum = -1

        for right in range(len(nums)):

            current_sum += nums[right]

            while current_sum > target:
                current_sum -= nums[left]
                left += 1

            if current_sum == target:
                maximum = max(maximum, right - left + 1)

        if maximum == -1:
            return -1

        return len(nums) - maximum
