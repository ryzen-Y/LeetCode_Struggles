class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        return abs(n - 1000) + 1
