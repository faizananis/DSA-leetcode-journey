class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        my_set=set()
        result=[]
        for num in nums:
            my_set.add(num)
        for i in range(1,len(nums)+1):
            if i not in my_set:
                result.append(i)
        return result
