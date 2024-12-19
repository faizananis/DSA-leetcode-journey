class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_seen=-1
        count=0
        for i in range(len(arr)):
            max_seen=max(max_seen,arr[i])
            if max_seen==i:
                count+=1
        return count