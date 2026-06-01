class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        buy = 0

        for i in range(1, len(prices)):
            if prices[buy] < prices[i]:
                profit = max(profit, prices[i] - prices[buy])
            else:
                buy = i

        return profit