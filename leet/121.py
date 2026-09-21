from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in prices:
            min_price = min(i, min_price)
            profit = i - min_price
            max_profit = max(profit, max_profit)
        return max_profit

# sliding window approch


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = 0
        sell = 1
        n = len(prices)
        maximum = 0

        while sell < n:

            if prices[sell] < prices[buy]:
                buy = sell
            else:
                profit = prices[sell] - prices[buy]
                maximum = max(maximum, profit)
        return maximum
