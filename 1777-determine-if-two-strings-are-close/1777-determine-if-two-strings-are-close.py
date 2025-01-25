class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        arr1=[0]*26
        arr2=[0]*26
        if len(word1)!=len(word2):
            return False
        for c in word1:
            arr1[ord(c)-ord('a')]+=1
        for c in word2:
            arr2[ord(c)-ord('a')]+=1
        for i in range(26):
            if arr1[i]==0 and arr2[i]>0:
                return False
            elif arr1[i]>0 and arr2[i]==0:
                return False
        return True

