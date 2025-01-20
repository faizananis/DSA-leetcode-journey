class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        # Step-1: Create a lookup for each value in the matrix
        lookup = {}  # Stores (x, y) coordinates for each element
        for i in range(m):
            for j in range(n):
                lookup[mat[i][j]] = (i, j)
        
        # Step-2: Find the earliest row or column painted
        row_count = [0] * m
        col_count = [0] * n
        
        for i, val in enumerate(arr):
            x, y = lookup[val]
            row_count[x] += 1
            col_count[y] += 1
            if row_count[x] == n or col_count[y] == m:
                return i
        
        return 0
