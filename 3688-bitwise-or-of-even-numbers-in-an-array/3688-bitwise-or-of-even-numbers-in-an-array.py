class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                res|=nums[i]
        return res