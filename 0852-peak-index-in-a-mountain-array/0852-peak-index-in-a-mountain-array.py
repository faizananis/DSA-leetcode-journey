class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left=0
        right=len(arr)-1
        peak=0
        while left<=right:
            mid=(left+right)//2
            if arr[peak]<arr[mid]:
                peak=mid
            if arr[mid]>arr[mid+1]:
                right=mid-1
            elif arr[mid]<arr[mid+1]:
                left=mid+1
        return peak