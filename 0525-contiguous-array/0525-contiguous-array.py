class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ones=0
        length=0
        maxLength=0
        prefix=0
        print(sum(nums),len(nums))
        for i in range(len(nums)-1,-1,-1):
            prefix+=nums[i]
            length+=1
            if length%2==0 and length//2==prefix:
                maxLength=max(maxLength,length)
        prefix=0
        length=0
        for i in range(len(nums)):
            prefix+=nums[i]
            length+=1
            if length%2==0 and length//2==prefix:
                maxLength=max(maxLength,length)
        prefix=0
        length=0
        n=len(nums)
        for i in range(len(nums)):
            if i%2==0:
                prefix+=nums[i]
            else:
                prefix+=nums[n-i-1]
            length+=1
            if length%2==0 and length//2==prefix:
                maxLength=max(maxLength,length)
        return maxLength
        

        
        