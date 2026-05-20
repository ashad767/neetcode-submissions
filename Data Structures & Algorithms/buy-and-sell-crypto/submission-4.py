class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices) < 2):
            return 0

        sell = prices[1];
        buy = prices[0];
        minNum = prices[0]

        for i in range(1, len(prices)):
            minNum = min(minNum, prices[i])
            if(prices[i] - buy < 0 and i <= prices.index(sell)):
                buy = prices[i]
            else:
                sell = max(sell, prices[i])

            if(prices[i] - minNum > sell - buy):
                sell = prices[i]
                buy = minNum
            
        return max(0, sell - buy)