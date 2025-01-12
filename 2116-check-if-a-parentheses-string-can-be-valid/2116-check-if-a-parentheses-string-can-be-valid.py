class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        wild_card=0
        op=0
        cl=0
        if len(s)%2==1:
            return False
        for i in range(len(s)):
            if locked[i]=='0':
                wild_card+=1
            elif s[i]=='(':
                op+=1
            else:
                cl+=1
            if wild_card<(cl-op):
                return False
        wild_card=0
        op=0
        cl=0
        for i in range(len(s)-1,-1,-1):
            if locked[i]=='0':
                wild_card+=1
            elif s[i]==')':
                cl+=1
            else:
                op+=1
            if wild_card<(op-cl):
                return False
        return True


                
