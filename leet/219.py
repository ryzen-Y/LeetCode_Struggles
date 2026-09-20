from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        file = {}

        for i in range(len(nums)):

            if nums[i] in file:
                if i - file[nums[i]] <= k:
                    return True
            file[nums[i]] = i
        return False


# sliding window aprochh

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:

        left = 0
        n = len(nums)

        window = set()

        for right in range(n):
            if nums[right] in window:
                return True
            window.add(nums[right])

            if abs(left - right) >= k:
                window.remove(nums[left])
                left += 1
        return False
