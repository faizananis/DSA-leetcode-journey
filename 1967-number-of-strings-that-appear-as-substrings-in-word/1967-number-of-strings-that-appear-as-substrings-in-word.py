class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        substrings=set()
        for i in range(len(word)):
            for j in range(i,len(word)):
                substrings.add(word[i:j+1])
        ans=0
        for pat in patterns:
            if pat in substrings:
                ans+=1
        return ans