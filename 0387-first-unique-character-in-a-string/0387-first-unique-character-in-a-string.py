class Solution:
    def firstUniqChar(self, s: str) -> int:
        queue=[]
        arr=[0]*26
        queue.append(0)
        for i in range(1,len(s)):
            if queue and s[i]==s[queue[0]]:
                arr[ord(s[i])-97]=1
                queue.pop(0)
            elif arr[ord(s[i])-97]==0:
                queue.append(i)
                arr[ord(s[i])-97]=1
        if queue:
            return queue[0]
        return -1