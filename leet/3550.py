class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        for index, value in enumerate(nums):
            add = 0
            for digits in str(value):
                add += int(digits)
            if add == index:
                return index
        return -1
