class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        nums_dict=Counter(nums)
        left=0
        window={}
        result=0
        n=len(nums)
        for right in range(len(nums)):
            if nums[right] not in window:
                window[nums[right]]=1
            else:
                window[nums[right]]+=1
            while len(window)==len(nums_dict):
                result+=n-right
                window[nums[left]]-=1
                if window[nums[left]]==0:
                    del window[nums[left]]
                left+=1
        return result