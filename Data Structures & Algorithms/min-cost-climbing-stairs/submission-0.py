class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for steps in range(2,len(cost)):
            cost[steps]+=min(cost[steps-1],cost[steps-2])
        return min(cost[-1],cost[-2])
        