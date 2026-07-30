from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count_1 = 0
        count_0 = 0
        count_2 = 0
        for i in nums:
            if i == 1:
                count_1 += 1
            elif i == 0:
                count_0 += 1
            elif i == 2:
                count_2 += 1
        nums[:] = [0] * count_0 + [1] * count_1 + [2] * count_2
