class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x=0
        y=0
        ans=0
        pos=0
        index=0
        direct=['N','E','S','W']
        s=set((i,j) for i,j in obstacles)
        for i in commands:
            if i==-1:
                pos+=1
                pos=pos%4
            elif i==-2:
                pos-=1
                pos=pos%4
            else:
                if pos==0:
                    for move in range(i):
                        if(x,y+1) in s:
                            break
                        y+=1
                elif pos==1:
                    for move in range(i):
                        if(x+1,y) in s:
                            break
                        x+=1
                elif pos==2:
                    for move in range(i):
                        if(x,y-1) in s:
                            break
                        y-=1
                else:
                    for move in range(i):
                        if(x-1,y) in s:
                            break
                        x-=1
                ans=max(ans,x**2+y**2)
                   # minX=min(minX,x)
            #x=max(maxX,minX*-1)
            #y=max(maxY,minY*-1)
        return ans
