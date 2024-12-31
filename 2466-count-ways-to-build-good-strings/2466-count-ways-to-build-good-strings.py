class Solution:
    def __init__(self):
        self.dp = [-1] * 100001
        self.MOD = 1000000007

    def countWays(self, low, high, zero, one, pos):
        if pos > high:
            return 0
        if self.dp[pos] != -1:
            return self.dp[pos]

        count = 0
        if pos >= low:
            count += 1
        count += self.countWays(low, high, zero, one, pos + zero)
        count += self.countWays(low, high, zero, one, pos + one)

        self.dp[pos] = count % self.MOD
        return self.dp[pos]

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        self.dp = [-1] * 100001
        return self.countWays(low, high, zero, one, 0)
    
        