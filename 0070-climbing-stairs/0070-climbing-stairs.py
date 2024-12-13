class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1]*n
        def climb(n):
            if n==0 or n==1:
                return 1
            if n not in dp:
                dp[n]=climb(n-1)+climb(n-2)
            return dp[n]
        return climb(n-1)+climb(n-2)