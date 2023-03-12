# similar questions:
# 91. Decode Ways
# 62. Unique Paths
# 509. Fibonacci Number

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        elif n == 0:
            return 1
        
        return self.climbStairs(n-1) + self.climbStairs(n-2)
    

    # simple DP concept
    def climbStairs2(self, n: int) -> int:
        prior2, prior1 = 0, 1
        for i in range(1, n+1):
            cur = prior2 + prior1
            prior2 = prior1
            prior1 = cur

        return prior1

        
            

