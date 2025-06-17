class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7

        # Check if it's impossible to reach the target with the given number of dice and faces
        if n * k < target:
            return 0

        # Initialize a 2D list to store the number of ways to achieve each target sum using a specific number of dice
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        # Dynamic Programming: Iterate over the number of dice and target sums
        for i in range(1, n + 1):
            for j in range(i, min(i * k, target) + 1):
                for temp in range(1, min(k, j) + 1):
                    # Update the number of ways to achieve the current target sum
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - temp]) % MOD

        # Return the result, cast to integer
        return int(dp[n][target])
        