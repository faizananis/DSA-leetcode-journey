class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        start=0
        end=0
        res=[]
        for i in range(len(nums)):
            if nums[i]==key:
                start=max(i-k,0)
                end=min(i+k,len(nums)-1)
                res+=range(start,end+1)
        return list(set(res))
            