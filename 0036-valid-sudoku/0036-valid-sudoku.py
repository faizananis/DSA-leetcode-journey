class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        my_set=[set() for _ in range(27)]
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue
                val = board[i][j]
                row=i
                col=9+j
                box=18+(i//3)*3+(j//3)
                if val in my_set[i] or val in my_set[col] or val in my_set[box]:
                    return False
                my_set[row].add(val)
                my_set[col].add(val)
                my_set[box].add(val)
        return True
