import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap=[]
        for i in range(len(nums)):
            heapq.heappush(heap,(nums[i],i))
        for _ in range(k):
            mini,index=heapq.heappop(heap)
            heapq.heappush(heap,(mini*multiplier,index))
        while heap:
            val,index=heapq.heappop(heap)
            nums[index]=val
        return nums
