class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        arr=[0]*len(nums)
        for l,r in queries:
            arr[l]+=1
            if r+1<len(nums):
                arr[r+1]-=1
        for i in range(1,len(arr)):
            arr[i]+=arr[i-1]
        for i in range(len(nums)):
            nums[i]-=arr[i]
            if nums[i]>0:
                return False
        return True
