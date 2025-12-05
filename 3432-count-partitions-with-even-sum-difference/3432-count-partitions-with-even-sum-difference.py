class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        left_sum=0
        right_sum=sum(nums)
        ans=0
        for i in range(len(nums)-1):
            left_sum+=nums[i]
            right_sum-=nums[i]
            diff=right_sum-left_sum
            if diff%2==0:
                ans+=1
        return ans
