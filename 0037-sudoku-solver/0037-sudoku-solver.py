class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Initialize sets with existing numbers
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i // 3) * 3 + (j // 3)].add(val)

        def backtrack(r, c):
            if r == 9:
                return True
            if c == 9:
                return backtrack(r + 1, 0)
            if board[r][c] != '.':
                return backtrack(r, c + 1)

            for k in map(str, range(1, 10)):
                box_index = (r // 3) * 3 + (c // 3)
                if k not in rows[r] and k not in cols[c] and k not in boxes[box_index]:
                    board[r][c] = k
                    rows[r].add(k)
                    cols[c].add(k)
                    boxes[box_index].add(k)

                    if backtrack(r, c + 1):
                        return True

                    # undo
                    board[r][c] = '.'
                    rows[r].remove(k)
                    cols[c].remove(k)
                    boxes[box_index].remove(k)
            return False

        backtrack(0, 0)
