class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)

        score=0

        for _ in range(k):
            maxVal = -heapq.heappop(maxHeap)
            score+=maxVal
            heapq.heappush(maxHeap, -math.ceil(maxVal/3))

        return score


        # score=0
        # while k>0:
        #     val=0
        #     index=-1
        #     for i in range(len(nums)):
        #         if val<nums[i]:
        #             val=nums[i]
        #             index=i
        #     score+=nums[index]
        #     if nums[index]%3==0:
        #         nums[index]//=3
        #     else:
        #         nums[index]=nums[index]//3+1
        #     k-=1
        # return score