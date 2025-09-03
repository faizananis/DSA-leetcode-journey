class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr=[0]*26
        for char in s:
            arr[ord(char)-97]+=1
        for char in t:
            arr[ord(char)-97]-=1
        for i in range(26):
            if arr[i]!=0:
                return False
        return True