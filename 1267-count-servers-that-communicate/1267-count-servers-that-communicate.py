class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_count = [0] * m
        col_count = [0] * n
        
        # Step 1: Count frequency of each row & column
        total_servers = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
                    total_servers += 1
        
        # Step 2: Check non-communicating servers
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    total_servers -= 1
        
        return total_servers

        # my_set=set()
        # m=len(grid)
        # n=len(grid[0])
        # count=0
        # count1=0
        # check=0
        # for i in range(m):
        #     check=0
        #     for j in range(n):
        #         if grid[i][j]==1:
        #             if check>=1 or j in my_set:
        #                 count+=1
        #                 check+=1
        #             my_set.add(j)
        #     if check>1:
        #         count+=1
        # return count

