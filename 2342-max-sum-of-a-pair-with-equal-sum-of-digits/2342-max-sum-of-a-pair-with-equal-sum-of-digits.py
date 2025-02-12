class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        my_heap=[]
        arr=[]
        for num in nums:
            digits_sum=0
            value=num
            while value:
                digits_sum+=value%10
                value//=10
            arr.append(digits_sum)
        for i in range(len(nums)):
            heapq.heappush(my_heap,(-arr[i],nums[i]))
        count=0
        temp=-1
        ans=[]
        prevNum=-1
        prevValue=-1
        if len(my_heap)<2:
            return -1
        while my_heap:
            num,value=heapq.heappop(my_heap)
            if prevNum==num:
                ans.append(prevValue+value)
            prevNum=num
            prevValue=value
        if ans:
            return ans[0]
        return -1
        



        