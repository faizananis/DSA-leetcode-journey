class Solution:
    def smallestNumber(self, n: int) -> int:
        arr=[1,3,7,15,31,63,127,255,511,1023]
        left=0
        right=len(arr)-1
        while left<right:
            mid=(left+right)//2
            if arr[mid]>=n:
                right=mid
            else:
                left=mid+1
        return arr[right]
            