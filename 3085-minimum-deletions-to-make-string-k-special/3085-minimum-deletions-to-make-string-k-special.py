class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        my_dict=Counter(word)
        arr=list(my_dict.values())
        result=0
        print(arr)
        if len(arr)==1:
            return 0
        if len(arr)==2 and abs(arr[1]-arr[0])>k:
            return min(arr)
        for i in range(1,len(arr)):
            if abs(arr[i]-arr[i-1])>k:
                result+=abs(arr[i]-arr[i-1])-k
        return result
            