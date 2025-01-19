import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        def is_valid(x, y, m, n):
            return 0 <= x < m and 0 <= y < n

        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:  # Need minimum 3x3 matrix to hold water
            return 0

        # Step-1: Push all boundary elements as START points
        min_heap = []
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(min_heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        # Step-2: Apply BFS similar to level-order traversal
        level = 0
        trapped_water = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        while min_heap:
            height, x, y = heapq.heappop(min_heap)
            level = max(level, height)

            for dx, dy in directions:
                newX, newY = x + dx, y + dy
                if is_valid(newX, newY, m, n) and not visited[newX][newY]:
                    visited[newX][newY] = True
                    heapq.heappush(min_heap, (heightMap[newX][newY], newX, newY))
                    if heightMap[newX][newY] < level:
                        trapped_water += level - heightMap[newX][newY]

        return trapped_water
        