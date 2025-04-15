class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.slidingWindowAtMost(nums, k) - self.slidingWindowAtMost(nums, k - 1)

    def slidingWindowAtMost(self, nums: List[int], distinctK: int) -> int:
        freq = {}
        left = 0
        total_count = 0

        for right in range(len(nums)):
            if nums[right] in freq:
                freq[nums[right]]+=1
            else:
                freq[nums[right]]=1

            while len(freq) > distinctK:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            total_count += right - left + 1

        return total_count 
        