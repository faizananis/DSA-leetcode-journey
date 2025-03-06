class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        arr=[0]*((n*n)+1)
        for i in range(n):
            for j in range(n):
                arr[grid[i][j]]+=1
        a=0
        b=0
        for i in range(len(arr)):
            if arr[i]==0:
                b=i
            if arr[i]==2:
                a=i
        return [a,b]
                
