class Solution:
    def minimumLength(self, s: str) -> int:
        left=0
        right=len(s)-1
        while left<right and s[left]==s[right]:
            ch=s[right]
            while left<=right and ch==s[left]:
                left+=1
            while left<=right and ch==s[right]:
                right-=1
        return right-left+1
