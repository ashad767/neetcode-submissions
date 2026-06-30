class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        cost.append(0)

        # bottom-up (backwards)
        # for c in range(len(cost) - 3, -1, -1):
        #     cost[c] = min(cost[c+1], cost[c+2]) + cost[c]
        
        # return min(cost[0], cost[1])

        # top-down (forwards)
        for c in range(2, len(cost)):
            cost[c] = min(cost[c-1], cost[c-2]) + cost[c]
        
        print(cost)

        return cost[len(cost)-1]