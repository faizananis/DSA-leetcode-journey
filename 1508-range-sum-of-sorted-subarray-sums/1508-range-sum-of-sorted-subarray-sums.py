class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        total_sums=[]
        for i in range(len(nums)):
            sums=0
            for j in range(i,len(nums)):
                sums+=nums[j]
                total_sums.append(sums)
        return sum(sorted(total_sums)[left-1:right])%(10**9+7)



        