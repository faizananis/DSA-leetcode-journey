class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        peak=0
        index=-1
        for i in range(len(arr)):
            if peak<arr[i]:
                peak=arr[i]
                index=i
        return index