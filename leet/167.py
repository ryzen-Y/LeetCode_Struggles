from typing import List


class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        left, right = 0, len(num) - 1

        while left < right:
            if num[left] + num[right] == target:
                return left, right
            elif num[left] + num[right] < target:
                left += 1
            else:
                right -= 1
