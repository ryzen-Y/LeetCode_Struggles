from typing import List


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []

        for i in range(len(nums)):
            if i % 2 == 0:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return arr1 + arr2
