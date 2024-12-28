class Solution:
    def __init__(self):
        self.prefix_sum = []
        self.mem = []

    def find_max_sum(self, nums, pos, count, k):
        if count == 3:
            return 0
        if pos > len(nums) - k:
            return 0
        if self.mem[pos][count] != -1:
            return self.mem[pos][count]

        # Don't start subarray here
        dont_start = self.find_max_sum(nums, pos + 1, count, k)

        # Start subarray here
        start_here = self.find_max_sum(nums, pos + k, count + 1, k) + self.prefix_sum[pos + k] - self.prefix_sum[pos]

        self.mem[pos][count] = max(dont_start, start_here)
        return self.mem[pos][count]

    def find_max_sum_path(self, nums, pos, count, k, path):
        if count == 3:
            return
        if pos > len(nums) - k:
            return

        # Don't start subarray here
        dont_start = self.find_max_sum(nums, pos + 1, count, k)

        # Start subarray here
        start_here = self.find_max_sum(nums, pos + k, count + 1, k) + self.prefix_sum[pos + k] - self.prefix_sum[pos]

        # Choose optimal path
        if start_here >= dont_start:
            path.append(pos)
            self.find_max_sum_path(nums, pos + k, count + 1, k, path)  # Include pos
        else:
            self.find_max_sum_path(nums, pos + 1, count, k, path)  # Don't include pos

    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        self.mem = [[-1] * 3 for _ in range(n)]

        # Calculate Prefix-Sum
        self.prefix_sum = [0] * (n + 1)
        for i in range(n):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

        # Find max_sum value
        self.find_max_sum(nums, 0, 0, k)

        # Find subarray start indices with max_sum value
        path = []
        self.find_max_sum_path(nums, 0, 0, k, path)

        return path
    
        