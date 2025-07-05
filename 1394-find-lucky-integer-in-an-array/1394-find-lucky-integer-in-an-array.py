class Solution:
    def findLucky(self, arr: List[int]) -> int:
        my_dict=Counter(arr)
        ans=-1
        for i in range(len(arr)):
            if arr[i]==my_dict[arr[i]]:
                ans=max(ans,arr[i])
        return ans