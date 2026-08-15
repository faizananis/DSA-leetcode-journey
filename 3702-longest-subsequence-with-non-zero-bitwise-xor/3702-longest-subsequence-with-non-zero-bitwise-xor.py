class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor = 0
        if sum(nums)==0:
            return 0
        for x in nums:
            total_xor ^= x
        
        if total_xor != 0:
            return len(nums)
        else:
            return len(nums) - 1

            
            