class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum = 0
        product = 1
        original = n

        while n > 0:
            digits = n % 10
            sum += digits
            product *= digits
            n //= 10
        return original % (sum + product) == 0
