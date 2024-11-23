class Solution:
    def fill(self,res, count, x, y):
        while count>0:
            res[x][y]='#'
            x-=1
            count-=1
    
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m=len(box)
        n=len(box[0])
        
        result = [['.' for _ in range(m)] for _ in range(n)]

        for i in range(m):
            count=0
            for j in range(n):
                if box[i][j]=='#':
                    count+=1
                elif box[i][j]=='*':
                    result[j][m-i-1]='*'
                    self.fill(result,count,j-1,m-i-1)
                    count=0
            if count>0:
                self.fill(result,count,n-1,m-i-1)
        return result