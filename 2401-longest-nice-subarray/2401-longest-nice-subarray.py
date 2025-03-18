class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left=0
        maxSize=0
        sums=0
        xor=0
        for right in range(len(nums)):
            sums+=nums[right]
            xor^=nums[right]
            if xor<sums:
                while xor!=sums:
                    sums-=nums[left]
                    xor^=nums[left]
                    left+=1
            maxSize=max(maxSize,right-left+1)
        return maxSize
        