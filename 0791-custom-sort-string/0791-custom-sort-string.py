class Solution:
    def customSortString(self, order: str, s: str) -> str:
        arr=[0]*26
        result=[]
        for c in s:
            arr[ord(c)-ord('a')]+=1
        for c in order:
            if arr[ord(c)-ord('a')]>0:
                for _ in range(arr[ord(c)-ord('a')]):
                    result.append(c)
                arr[ord(c)-ord('a')]=0
        for i in range(26):
            if arr[i]>0:
                for _ in range(arr[i]):
                    result.append(chr(i+ord('a')))
        return "".join(result)
