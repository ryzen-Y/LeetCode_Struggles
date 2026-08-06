class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            mul = 1

            for i in str(n):
                mul *= int(i)

            if mul % t == 0:
                return n

            n += 1