class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        prev=None
        for i in range(len(nums)-2):
            if prev==nums[i]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                summ=nums[i]+nums[l]+nums[r]
                if summ==0:
                    ans.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
                elif summ>0:
                    r-=1
                elif summ<0:
                    l+=1
            prev=nums[i]
        return ans
                