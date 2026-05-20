class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1

        maxProfit = 0

        while left < len(prices) - 1:
            if prices[right] > prices[left]:
                currProfit = prices[right] - prices[left]
                if maxProfit < currProfit:
                    maxProfit = currProfit

            right += 1
            if right >= len(prices):
                left += 1
                right = left + 1

        return maxProfit