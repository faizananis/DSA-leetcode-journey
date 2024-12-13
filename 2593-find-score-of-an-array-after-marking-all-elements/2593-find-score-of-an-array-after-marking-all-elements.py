class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap=[]
        score=0
        for i in range(len(nums)):
            heapq.heappush(heap,(nums[i],i))
        my_set=set()
        while len(my_set)<len(nums):
            val,index=heapq.heappop(heap)
            if index not in my_set:
                score+=val
            else:
                continue
            my_set.add(index)
            if index>0 and index<len(nums)-1:
                my_set.add(index-1)
                my_set.add(index+1)
            elif index>0:
                my_set.add(index-1)
            else:
                my_set.add(index+1)
        return score
            
