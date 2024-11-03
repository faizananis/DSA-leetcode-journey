class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        if s==goal:
            return True
        for i in range(len(s)):
            k=i
            for j in range(len(s)):
                if s[k]!=goal[j]:
                    break
                k+=1
                if(k==len(s)):
                    k=0
            else:
                return True
        return False