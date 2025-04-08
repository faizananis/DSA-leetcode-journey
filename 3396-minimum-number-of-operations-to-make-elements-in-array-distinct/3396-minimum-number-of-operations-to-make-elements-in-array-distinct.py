class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        my_set=set()
        ptr=0
        for i in range(len(nums)):
            if nums[i] in my_set:
                ptr=i
            else:
                my_set.add(nums[i])
        return math.ceil(ptr/3)