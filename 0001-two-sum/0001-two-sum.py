class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict={}
        for i in range(len(nums)):
            if target-nums[i] in my_dict:
                return [my_dict[target-nums[i]],i]
            else:
                my_dict[nums[i]]=i
        
            








        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        
        # my_dict={}
        # for i in range(len(nums)):
        #     if target-nums[i] in my_dict:
        #         return [my_dict[target-nums[i]],i]
        #     my_dict[nums[i]]=i