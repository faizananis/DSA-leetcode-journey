from itertools import accumulate

class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        n = len(grid[0])
        if n < 2:
            return 0

        top_sum = sum(grid[0])
        bottom_sum = 0
        min_sum = float('inf')

        for pp in range(n):
            top_sum -= grid[0][pp]
            min_sum = min(min_sum, max(top_sum, bottom_sum))
            bottom_sum += grid[1][pp]

        return min_sum
        