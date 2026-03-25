class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total_sum=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                total_sum+=grid[i][j]
        
        row_sum=0
        col_sum=0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                row_sum+=grid[i][j]
            if row_sum==total_sum-row_sum:
                return True
        
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                col_sum+=grid[j][i]
            if col_sum==total_sum-col_sum:
                return True
        
        return False