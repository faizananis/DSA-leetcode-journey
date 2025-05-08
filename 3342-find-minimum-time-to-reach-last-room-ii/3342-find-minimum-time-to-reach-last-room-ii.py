class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Initialize result matrix with infinity
        result = [[float('inf')] * n for _ in range(m)]
        result[0][0] = 0

        # Min-heap: (time, i, j)
        pq = [(0, 0, 0)]

        while pq:
            currTime, i, j = heapq.heappop(pq)

            # If we reached bottom-right corner
            if i == m - 1 and j == n - 1:
                return currTime

            for dx, dy in directions:
                i_, j_ = i + dx, j + dy
                if 0 <= i_ < m and 0 <= j_ < n:
                    moveCost = 2 if (i_ + j_) % 2 == 0 else 1
                    wait = max(moveTime[i_][j_] - currTime, 0)
                    arrTime = currTime + wait + moveCost

                    if arrTime < result[i_][j_]:
                        result[i_][j_] = arrTime
                        heapq.heappush(pq, (arrTime, i_, j_))

        return -1