class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        count=0
        sum1=0
        my_set=set(banned)
        for i in range(1,n+1):
            if i not in my_set:
                if sum1+i<=maxSum:
                    sum1+=i
                    count+=1
                else:
                    break
        return count