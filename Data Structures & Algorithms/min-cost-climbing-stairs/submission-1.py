class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costs = [0] * (len(cost) + 2)
        cost.append(0)
        cost.append(0)

        for c in range(2, len(costs)):
            costs[c] = min(cost[c-1] + costs[c - 1], cost[c-2] + costs[c - 2])
        
        print(costs, cost)
        return costs[len(costs)-1]