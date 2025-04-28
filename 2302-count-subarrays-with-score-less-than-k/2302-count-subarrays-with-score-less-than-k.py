class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left=0
        score=0
        window=0
        ans=0
        for right in range(len(nums)):
            score+=nums[right]
            window=right-left+1
            while score*window>=k and left<right:
                score-=nums[left]
                left+=1
                window-=1
            if score*window<k:
                ans+=window
        return ans