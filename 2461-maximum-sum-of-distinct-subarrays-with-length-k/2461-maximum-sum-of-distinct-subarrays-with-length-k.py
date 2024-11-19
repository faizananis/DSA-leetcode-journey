class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left=0
        right=0
        sums=0
        maxSum=0
        n=len(nums)
        freq={}
        while right<k:
            if nums[right] in freq:
                freq[nums[right]]+=1
            else:
                freq[nums[right]]=1
            sums+=nums[right]
            right+=1
        right-=1
        while right<n-1:
            if len(freq)==k:
                maxSum=max(maxSum,sums)
            freq[nums[left]]-=1
            if freq[nums[left]]==0:
                del freq[nums[left]]
            sums-=nums[left]
            left+=1
            right+=1
            sums+=nums[right]
            if nums[right] in freq:
                freq[nums[right]]+=1
            else:
                freq[nums[right]]=1
        return maxSum