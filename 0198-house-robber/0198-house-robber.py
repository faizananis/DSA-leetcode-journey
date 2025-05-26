class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        #memo={}
        @lru_cache(maxsize=None)
        def dp(i):
            if i >= n:
                return 0
            # if i in memo:
            #     return memo[i]
            # Rob current house or skip it
            rob = nums[i] + dp(i + 2)
            skip = dp(i + 1)
            return max(rob, skip)

        return dp(0)

        