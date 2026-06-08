class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costs = cost + [0]

        for c in range(len(costs) - 3, -1, -1):
            costs[c] = min(costs[c+1], costs[c+2]) + cost[c]
        
        return min(costs[0], costs[1])