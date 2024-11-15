class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        left=0
        n=len(arr)
        right=n-1

        while arr[right-1]<=arr[right] and right>0:
            right-=1

        shortest=right
        while left<right:
            while right<n and arr[left]>arr[right]:
                right+=1

            shortest = min(shortest,right-left-1)
            left+=1

            if arr[left]<arr[left-1]:
                break
        
        return shortest
