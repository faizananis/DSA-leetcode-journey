class Solution:
    def findGCD(self, nums: List[int]) -> int:
        num1=min(nums)
        num2=max(nums)
        div=min(num1,num2)
        while div>1:
            if num1%div==0 and num2%div==0:
                return div
            div-=1
        return 1