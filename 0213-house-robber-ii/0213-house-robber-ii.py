class Solution:
    def rob(self, nums: list[int]) -> int:
        def rob_linear(start, end):
            memo = {}

            def dp(i):
                if i > end:
                    return 0
                if i in memo:
                    return memo[i]
                # Rob current or skip
                rob = nums[i] + dp(i + 2)
                skip = dp(i + 1)
                memo[i] = max(rob, skip)
                return memo[i]

            return dp(start)

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # Case 1: Exclude last house
        case1 = rob_linear(0, n - 2)
        # Case 2: Exclude first house
        case2 = rob_linear(1, n - 1)

        return max(case1, case2)
        