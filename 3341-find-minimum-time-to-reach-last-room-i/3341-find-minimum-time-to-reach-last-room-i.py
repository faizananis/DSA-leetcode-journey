class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Initialize result grid with large numbers
        result = [[float('inf')] * n for _ in range(m)]
        result[0][0] = 0

        # Min-heap: (time, i, j)
        heap = [(0, 0, 0)]

        while heap:
            currTime, i, j = heapq.heappop(heap)

            if i == m - 1 and j == n - 1:
                return currTime  # reached destination

            for di, dj in directions:
                ni, nj = i + di, j + dj

                if 0 <= ni < m and 0 <= nj < n:
                    # Calculate wait time if we arrive too early
                    wait = max(moveTime[ni][nj] - currTime, 0)
                    arrTime = currTime + wait + 1  # +1 because we move 1 step

                    # Relax the cell if found a better (smaller) time
                    if arrTime < result[ni][nj]:
                        result[ni][nj] = arrTime
                        heapq.heappush(heap, (arrTime, ni, nj))

        return -1  # if no path (shouldn't happen here)