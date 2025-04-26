class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        min_k=-1
        max_k=-1
        culprit=-1
        ans=0

        for i in range(len(nums)):
            if nums[i]<minK or nums[i]>maxK:
                culprit=i
            if nums[i]==minK:
                min_k=i
            if nums[i]==maxK:
                max_k=i
            smaller=min(min_k,max_k)
            temp=smaller-culprit
            if temp>=0:
                ans+=temp
        return ans
