import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        left = 1
        right = max(piles)
        minimum = right

        while left <= right:
            mid = (left + right) // 2
            add = 0
            for p in piles:
                add += math.ceil(p / mid)

            if add <= h:
                minimum = min(minimum, mid)
                right = mid - 1
            else:
                left = mid + 1

        return minimum
