class Solution:
    def checkRecord(self, s: str) -> bool:
        countA=0
        countL=0
        for i in s:
            if i=='A':
                countA+=1
                countL=0
            elif i=='L':
                countL+=1
            else:
                countL=0
            if countA==2 or countL==3:
                return False
        return True