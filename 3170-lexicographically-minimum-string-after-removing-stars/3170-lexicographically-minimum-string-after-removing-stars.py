class Solution:
    def clearStars(self, s: str) -> str:
        heap=[]
        s=list(s)
        ans=""
        for i in range(len(s)):
            if s[i]=='*':
                s[-heapq.heappop(heap)[1]]='*'
            else:
                heapq.heappush(heap,(s[i],-i))
        for c in s:
            if c=='*':
                continue
            ans+=c
        return ans