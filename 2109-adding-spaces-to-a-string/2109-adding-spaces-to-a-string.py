class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result=""
        n=0
        for i in range(len(s)):
            if n<len(spaces) and i==spaces[n]:
                result+=' '
                n+=1
            result+=s[i]
        return result