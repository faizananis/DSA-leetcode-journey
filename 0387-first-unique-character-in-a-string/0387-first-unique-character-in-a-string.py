class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = defaultdict(int)
        for i in s:
            dic[i]+=1
        ind = 0
        q = deque()
        for j in s:
            q.append(j)
            while q:
                if dic[q[0]]>1:
                    q.popleft()
                    ind+=1
                else:
                    break
        if ind<len(s):
            return ind
        else:
            return -1