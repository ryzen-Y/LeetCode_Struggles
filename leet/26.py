class Solution:
    def removeDuplicates(self, nums):

        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow], nums[fast] = nums[fast], nums[slow]
        return slow + 1
