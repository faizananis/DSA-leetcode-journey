class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        height = [[0] * n for _ in range(m)]
        queue = deque()

        # Step-1: Push all start points for Multi-Source BFS
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    queue.append((i, j))
                    visited[i][j] = True

        # Step-2: Multi-Source BFS Levelorder
        dir = [-1, 0, 1, 0]  # 4-directional calls: URDL
        level = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()

                for d in range(4):
                    newX, newY = x + dir[d], y + dir[(d + 1) % 4]
                    if self.isValid(newX, newY, m, n) and not visited[newX][newY]:
                        queue.append((newX, newY))
                        height[newX][newY] = 1 + level
                        visited[newX][newY] = True
            level += 1

        return height

    def isValid(self, x, y, m, n):
        return 0 <= x < m and 0 <= y < n