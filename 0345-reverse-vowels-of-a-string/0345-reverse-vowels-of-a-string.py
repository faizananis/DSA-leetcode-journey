class Solution:
    def reverseVowels(self, s: str) -> str:
        stack=[]
        vowels="aeiouAEIOU"
        for c in s:
            if c in vowels:
                stack.append(c)
        s=list(s)
        for i in range(len(s)):
            if s[i] in vowels:
                s[i]=stack.pop()

        return "".join(s)
