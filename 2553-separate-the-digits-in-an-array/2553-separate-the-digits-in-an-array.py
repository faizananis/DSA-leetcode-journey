class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        def find_digits(n):
            if n==0:
                return 0
            find_digits(n//10)
            ans.append(n%10)
        for num in nums:
            find_digits(num)
        return ans
