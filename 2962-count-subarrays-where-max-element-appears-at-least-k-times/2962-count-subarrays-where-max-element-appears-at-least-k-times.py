class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        value=max(nums)
        window=0
        left=0
        count=0
        result=0
        for right in range(len(nums)):
            if nums[right]==value:
                count+=1
            window=right-left+1
            while count>=k and left<=right:
                result+=len(nums)-right
                if nums[left]==value:
                    count-=1
                left+=1
        return result
            
                
        