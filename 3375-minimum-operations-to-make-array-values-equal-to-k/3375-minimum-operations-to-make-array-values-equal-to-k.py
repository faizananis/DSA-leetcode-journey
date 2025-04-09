class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        my_set=set()
        for n in nums:
            if n<k:
                return -1
            if n > k:
                my_set.add(n)
        return len(my_set)