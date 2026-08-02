from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        memo = {}

        def f(left, right):

            if left > right:
                return 0

            if (left, right) in memo:
                return memo[(left, right)]

            lefty = piles[left] - f(left + 1, right)
            righty = piles[right] - f(left, right - 1)

            memo[(left, right)] = max(lefty, righty)

            return memo[(left, right)]

        return f(0, n - 1) > 0
