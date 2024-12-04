class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n=0
        for i in range(len(str1)):
            if str1[i]==str2[n] or ord(str1[i])+1==ord(str2[n]) or ord(str1[i])-25==ord(str2[n]):
                n+=1
            if n==len(str2):
                return True
        return False