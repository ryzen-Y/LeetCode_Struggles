from typing import List


class Solution:
    def reverse(self, nums, left, right):

        while left < right:

            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def rotate(self, nums: List[int], k: int) -> None:

        n = len(nums)

        k = k % n
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, k, n - 1)
        self.reverse(nums, 0, k - 1)


# ======== Slicing Method ========


class Solution:
    def reverse(self, nums, left, right):

        n = len(nums)

        k %= n

        if k != 0:
            arr = nums[n-k:]
            del nums[n-k:]
            nums[0:0] = arr
