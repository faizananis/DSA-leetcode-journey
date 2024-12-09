class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        result=[]
        flag=0
        prefix_sum=[1]*len(nums)
        flag=nums[0]%2
        for i in range(1,len(nums)):
            if flag!=nums[i]%2:
                prefix_sum[i]+=prefix_sum[i-1]
            flag=nums[i]%2
        
        for i in queries:
            diff=i[1]-i[0]
            if prefix_sum[i[1]]>=diff:
                result.append(True)
            else:
                result.append(False)
        return result





        
        # for i in queries:
        #     start=i[0]
        #     end=i[1]
        #     flag=nums[start]%2
        #     for j in range(start+1,end+1):
        #         if flag==nums[j]%2:
        #             result.append(False)
        #             break
        #         flag=nums[j]%2
        #     else:
        #         result.append(True)
        # return result