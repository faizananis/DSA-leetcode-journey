class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left=0
        sums=0
        maxSum=0
        my_dict={}
        for right in range(len(nums)):
            if nums[right] in my_dict:
                my_dict[nums[right]]+=1
            else:
                my_dict[nums[right]]=1
            while len(my_dict)<right-left+1:
                if my_dict[nums[left]]==1:
                    del my_dict[nums[left]]
                else:
                    my_dict[nums[left]]-=1
                sums-=nums[left]
                left+=1
            sums+=nums[right]
            maxSum=max(maxSum,sums)
        return maxSum