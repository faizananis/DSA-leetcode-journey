class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}  # key: remaining amount, value: min number of coins

        def dp(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return float('inf')
            if rem in memo:
                return memo[rem]

            min_coins = float('inf')
            for coin in coins:
                res = dp(rem - coin)
                if res != float('inf'):
                    min_coins = min(min_coins, 1 + res)

            memo[rem] = min_coins
            return memo[rem]

        result = dp(amount)
        return -1 if result == float('inf') else result

        # dp = [amount + 1] * (amount + 1)
        # dp[0] = 0

        # for a in range(1, amount + 1):
        #     for c in coins:
        #         if a - c >= 0:
        #             dp[a] = min(dp[a], 1 + dp[a - c])
        # return dp[amount] if dp[amount] != amount + 1 else -1