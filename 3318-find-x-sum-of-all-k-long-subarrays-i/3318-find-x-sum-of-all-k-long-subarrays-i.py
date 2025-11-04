class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        my_hash={}
        x_sum=0
        ans=[]
        left=0
        right=0
        n=len(nums)
        pq=[]
        while right<k:
            if nums[right] not in my_hash:
                my_hash[nums[right]]=1
            else:
                my_hash[nums[right]]+=1
            right+=1
        right-=1
        while right<n:
            flag=1
            pq=[]
            x_sum=0
            right+=1
            for val in my_hash:
                heapq.heappush(pq,(my_hash[val],val))
            i=0
            while len(pq)>x:
                heapq.heappop(pq)
            while pq:
                item=heapq.heappop(pq)
                x_sum+=item[0]*item[1]
            ans.append(x_sum)
            if right<n:
                if nums[right] not in my_hash:
                    my_hash[nums[right]]=1
                else:
                    my_hash[nums[right]]+=1
                my_hash[nums[left]]-=1
                if my_hash[nums[left]]==0:
                    del my_hash[nums[left]]
                left+=1
        return ans

            
