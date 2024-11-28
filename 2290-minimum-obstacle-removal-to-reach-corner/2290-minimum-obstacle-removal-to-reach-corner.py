class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dir = [-1, 0, 1, 0, -1]
        visited = [[False] * n for _ in range(m)]
        
        minheap = []
        heappush(minheap, (0, 0, 0))  # (cost, x, y)
        visited[0][0] = True
        
        while minheap:
            cost, x, y = heappop(minheap)
            
            if x == m - 1 and y == n - 1:
                return cost
            
            for i in range(4):
                newX, newY = x + dir[i], y + dir[i + 1]
                if 0 <= newX < m and 0 <= newY < n and not visited[newX][newY]:
                    visited[newX][newY] = True
                    if grid[newX][newY] == 1:
                        heappush(minheap, (cost + 1, newX, newY))
                    else:
                        heappush(minheap, (cost, newX, newY))
        
        return 0