class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums[0]+nums[1]>nums[2] and nums[1]+nums[2]>nums[0] and nums[0]+nums[2]>nums[1]:
            s=set(nums)
            if len(s)==1:
                return "equilateral"
            elif len(s)==2:
                return "isosceles"
            else:
                return "scalene"
        else:
            return "none"
