class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sums=sum(nums)
        rem=sums%k
        return rem