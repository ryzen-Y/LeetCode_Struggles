class Solution:
    def maxArea(self, nums: list[int]) -> int:

        n = len(nums)
        left = 0
        right = n - 1
        maximum = 0

        while left < right:
            width = right - left
            height = min(nums[right], nums[left])
            area = width * height

            maximum = max(area, maximum)

            if nums[left] < nums[right]:
                left += 1
            else:
                right -= 1
        return maximum
