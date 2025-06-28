class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        arr=[]
        for i in range(len(nums)):
            heapq.heappush(arr,(-nums[i],i))
        result=[]
        for _ in range(k):
            a,b=heapq.heappop(arr)
            result.append([b,-a])
        result.sort()
        ans=[]
        for val in result:
            ans.append(val[1])
        return ans

