class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        row_s=float('inf')
        row_e=float('-inf')
        col_s=float('inf')
        col_e=float('-inf')

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    row_s=min(row_s,i)
                    row_e=max(row_e,i)
                    col_s=min(col_s,j)
                    col_e=max(col_e,j)
        return (row_e-row_s+1)*(col_e-col_s+1)