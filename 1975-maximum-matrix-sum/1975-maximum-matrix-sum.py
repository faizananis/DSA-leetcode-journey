class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        count=0
        n=len(matrix)
        sums=0
        minimum=float('inf')
        for i in range(n):
            for j in range(n):
                val=abs(matrix[i][j])
                minimum=min(minimum,val)
                sums+=val
                if matrix[i][j]<0:
                    count+=1
        if count%2==0:
            return sums
        return sums-minimum*2