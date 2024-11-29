class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        dir = [-1, 0, 1, 0, -1]
        m, n = len(grid), len(grid[0])
        if grid[0][1] > 1 + grid[0][0] and grid[1][0] > 1 + grid[0][0]:
            return -1

        visited = [[False] * n for _ in range(m)]
        min_heap = [(0, 0, 0)]  # (time, x, y)
        visited[0][0] = True

        while min_heap:
            time, x, y = heapq.heappop(min_heap)

            if x == m - 1 and y == n - 1:
                return time

            for i in range(4):
                newX, newY = x + dir[i], y + dir[i + 1]
                if 0 <= newX < m and 0 <= newY < n and not visited[newX][newY]:
                    visited[newX][newY] = True
                    new_time = time + 1
                    if grid[newX][newY] > new_time:
                        new_time = grid[newX][newY] if (grid[newX][newY] - time) % 2 == 1 else grid[newX][newY] + 1
                    heapq.heappush(min_heap, (new_time, newX, newY))

        return -1