class Solution:
    def numRescueBoats(self, nums: list[int], limit: int) -> int:

        nums.sort()
        n = len(nums)
        left = 0
        right = n - 1
        boat = 0

        while left <= right:
            sum = nums[left] + nums[right]

            if sum == limit:
                boat += 1
                left += 1
                right -= 1

            elif sum > limit:
                boat += 1
                right -= 1

            else:
                boat += 1
                left += 1
                right -= 1

        return boat
