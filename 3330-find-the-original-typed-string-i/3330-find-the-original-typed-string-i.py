class Solution:
    def possibleStringCount(self, word: str) -> int:
        count=0
        ans=0
        for i in range(1,len(word)):
            if word[i]==word[i-1]:
                count+=1
            else:
                ans+=count
                count=0
        return ans+count+1