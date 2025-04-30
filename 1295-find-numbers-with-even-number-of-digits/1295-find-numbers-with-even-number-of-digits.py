class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            number=nums[i]
            digits=0
            while number:
                number//=10
                digits+=1
            if digits%2==0:
                count+=1
        return count