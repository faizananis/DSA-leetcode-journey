class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans=float("inf")
        for n in nums:
            digit_sum=0
            while n:
                digit_sum+=n%10
                n//=10
            ans=min(digit_sum,ans)
        return ans