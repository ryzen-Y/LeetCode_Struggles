class Solution:
    def countCommas(self, n: int) -> int:

        if n < 1000:
            return 0

        if n < 1000000:
            return n - 999

        first = 999000
        second = n - 999999

        return first + second * 2
