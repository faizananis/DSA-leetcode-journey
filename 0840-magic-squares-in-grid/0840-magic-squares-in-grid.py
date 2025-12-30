class Solution:
    def isMagic(self, grid, i, j):
        my_set=set()
        sums=0
        for r in range(3):
            for c in range(3):
                if grid[i+r][j+c] in my_set or grid[i+r][j+c]==0 or grid[i+r][j+c]>9:
                    return False
        SUM=grid[i][j]+grid[i][j+1]+grid[i][j+2]
        for k in range(3):
            if grid[i][j+k]+grid[i+1][j+k]+grid[i+2][j+k]!=SUM:
                return False
            if grid[i+k][j]+grid[i+k][j+1]+grid[i+k][j+2]!=SUM:
                return False

        if grid[i][j]+grid[i+1][j+1]+grid[i+2][j+2]!=SUM:
            return False
        if grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j]!=SUM:
            return False
        
        return True

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count=0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                if self.isMagic(grid,i,j):
                    count+=1
        return count