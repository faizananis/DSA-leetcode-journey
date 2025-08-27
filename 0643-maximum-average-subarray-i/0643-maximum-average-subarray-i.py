class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i=0
        summ=0
        max_average=0
        for n in range(k):
            summ+=nums[n]

        max_average=summ/k
        for j in range(k,len(nums)):
            summ-=nums[i]
            summ+=nums[j]
            i+=1

            max_average=max(max_average,summ/k)
        return max_average
        


