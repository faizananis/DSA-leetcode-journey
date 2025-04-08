class Solution:
    def check(self,start,nums):
        my_set=set()
        for i in range(start,len(nums)):
            if nums[i] in my_set:
                return False
            my_set.add(nums[i])
        return True

    def minimumOperations(self, nums: List[int]) -> int:
        operation=0
        for i in range(0,len(nums),3):
            if self.check(i,nums):
                return operation
            operation+=1
        return operation