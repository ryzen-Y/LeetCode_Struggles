from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            dp[i] = float('-inf')

            current_sum = 0

            for j in range(i, min(i + 3, n)):
                current_sum += stoneValue[j]

                dp[i] = max(
                    dp[i],
                    current_sum - dp[j + 1]
                )

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
