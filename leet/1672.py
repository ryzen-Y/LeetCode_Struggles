from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = 0
        sum_1 = 0

        for rows in accounts:
            for i in rows:
                sum_1 = sum_1 + i
            maximum = max(maximum, sum_1)
            sum_1 = 0
        return maximum
