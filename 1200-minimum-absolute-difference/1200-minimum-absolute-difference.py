class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans=[]
        minimum=float("inf")
        for i in range(1,len(arr)):
            diff=arr[i]-arr[i-1]
            minimum=min(minimum,diff)
        for i in range(1,len(arr)):
            diff=arr[i]-arr[i-1]
            if diff==minimum:
                ans.append([arr[i-1],arr[i]])
        return ans
            