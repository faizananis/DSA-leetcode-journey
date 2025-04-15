class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.slidingWindowAtMost(nums, k) - self.slidingWindowAtMost(nums, k - 1)

    def slidingWindowAtMost(self, nums: List[int], distinctK: int) -> int:
        freq_map = {}
        left = 0
        total_count = 0

        for right in range(len(nums)):
            freq_map[nums[right]] += 1

            while len(freq_map) > distinctK:
                freq_map[nums[left]] -= 1
                if freq_map[nums[left]] == 0:
                    del freq_map[nums[left]]
                left += 1

            total_count += right - left + 1

        return total_count 
        