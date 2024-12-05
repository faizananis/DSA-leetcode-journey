class Solution:
    def canChange(self, start: str, target: str) -> bool:
        st=0
        tar=0
        while(st<len(start) and tar<len(target)):
            while(st<len(start)-1 and start[st]!='L' and start[st]!='R'):
                st+=1
            while(tar<len(target)-1 and target[tar]!='L' and target[tar]!='R'):
                tar+=1
            if start[st]!=target[tar]:
                return False
            if start[st]==target[tar]=='L':
                if st<tar:
                    return False
            if start[st]==target[tar]=='R':
                if st>tar:
                    return False
            st+=1
            tar+=1
        return True