class Solution:
    def climbStairs(self, n: int) -> int:
        ways=[1,1,2]

        for steps in range(3,n+1):
            ways.append(ways[steps-1]+ways[steps-2])
        return ways[n]
        