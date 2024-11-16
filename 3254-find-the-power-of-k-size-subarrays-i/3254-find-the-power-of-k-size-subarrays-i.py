class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        left=0
        right=0
        result=[]
        value=0
        while right<k-1:
            right+=1
        while right<len(nums):
            a=left
            b=right
            while a<b:
                if nums[a]+1!=nums[a+1]:
                    result.append(-1)
                    break
                a+=1
            if a==b:
                result.append(nums[a])
            left+=1
            right+=1
        return result