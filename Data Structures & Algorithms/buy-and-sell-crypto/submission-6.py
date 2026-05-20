class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        sell = 1

        for i in range(len(prices)):
            if prices[i] < prices[buy]:
                buy = i
                sell = i + 1
            elif i > sell and prices[i] > prices[sell]:
                sell = i
            
            if sell > len(prices) - 1:
                break

            profit = max(profit, prices[sell] - prices[buy])

        return profit