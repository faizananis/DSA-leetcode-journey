class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        i=0
        minimum=float("inf")
        for j in range(k-1,len(nums)):
            diff=nums[j]-nums[i]
            minimum=min(minimum,diff)
            i+=1
        return minimum


