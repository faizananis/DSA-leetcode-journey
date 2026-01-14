class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=0
        for i in range(32):
            bitsum=0
            for n in nums:
                bitsum+=(n>>i)&1
            if bitsum%3:
                result|=(1<<i)
        if result>2**31-1:
            result-=2*2**31
        return result