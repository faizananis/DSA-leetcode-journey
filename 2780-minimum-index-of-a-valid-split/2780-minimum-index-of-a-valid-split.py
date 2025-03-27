class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        map1={}
        map2={}
        size1=0
        size2=len(nums)
        for n in nums:
            if n in map2:
                map2[n]+=1
            else:
                map2[n]=1
        for i in range(len(nums)):
            map2[nums[i]]-=1
            size2-=1
            if nums[i] in map1:
                map1[nums[i]]+=1
            else:
                map1[nums[i]]=1
            size1+=1
            if map1[nums[i]]>size1//2 and map2[nums[i]]>size2//2:
                return i
        return -1
