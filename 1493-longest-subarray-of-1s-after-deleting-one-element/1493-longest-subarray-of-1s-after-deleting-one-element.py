class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left=0
        limit=0
        res=0
        window=0
        for right in range(len(nums)):
            if nums[right]==0:
                limit+=1
            while limit>1:
                if nums[left]==0:
                    limit-=1
                left+=1
            res=max(res,right-left+1-limit)
        if limit==0:
            return res-1
        return res