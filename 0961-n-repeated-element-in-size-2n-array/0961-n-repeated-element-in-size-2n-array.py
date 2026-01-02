class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        mydict=Counter(nums)
        count=len(nums)//2
        for val in mydict:
            if mydict[val]==count:
                return val
        
