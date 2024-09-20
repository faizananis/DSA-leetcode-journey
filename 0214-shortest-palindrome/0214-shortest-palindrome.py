class Solution:
    def shortestPalindrome(self, s: str) -> str:
        for i in range(len(s),0,-1):
            front=s[:i]
            rev=front[::-1]
            cur=s[i:]
            if front==rev:
                return cur[::-1]+s
        return ""