class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict1={}
        for n in nums:
            if n in dict1:
                return True
            dict1[n]=1
        return False