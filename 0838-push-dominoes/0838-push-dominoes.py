class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n=len(dominoes)
        leftClosest=[-1]*n
        rightClosest=[-1]*n
        result=""

        for i in range(n):
            if dominoes[i]=='R':
                leftClosest[i]=i
            elif dominoes[i]=='L':
                leftClosest[i]=-1
            elif i>0:
                leftClosest[i]=leftClosest[i-1]
        
        for i in range(n-1,-1,-1):
            if dominoes[i]=='L':
                rightClosest[i]=i
            elif dominoes[i]=='R':
                rightClosest[i]=-1
            elif i<n-1:
                rightClosest[i]=rightClosest[i+1]
        
        print(leftClosest)
        print(rightClosest)
        for i in range(n):
            if leftClosest[i]==rightClosest[i]==-1:
                result+='.'
            elif leftClosest[i]==-1:
                result+='L'
            elif rightClosest[i]==-1:
                result+='R'
            else:
                distLeft=abs(i-leftClosest[i])
                distRight=abs(i-rightClosest[i])
                if distLeft==distRight:
                    result+='.'
                else:
                    result+='R' if distLeft<distRight else 'L'

        return result