class Solution:
    def __init__(self):
        self.t = []  # Memoization table
        self.columnStates = []  # All valid column color patterns
        self.MOD = 10**9 + 7

    def generateColumnStates(self, currentColumn: str, rowsRemaining: int, prevColor: str):
        if rowsRemaining == 0:
            self.columnStates.append(currentColumn)
            return

        for color in ['R', 'G', 'B']:
            if color != prevColor:
                self.generateColumnStates(currentColumn + color, rowsRemaining - 1, color)

    def solve(self, remainingCols: int, prevColumnIdx: int, m: int) -> int:
        if remainingCols == 0:
            return 1
        if self.t[remainingCols][prevColumnIdx] != -1:
            return self.t[remainingCols][prevColumnIdx]

        totalWays = 0
        prevColumn = self.columnStates[prevColumnIdx]

        for nextColumnIdx, nextColumn in enumerate(self.columnStates):
            # Check horizontal adjacency
            if all(prevColumn[r] != nextColumn[r] for r in range(m)):
                totalWays = (totalWays + self.solve(remainingCols - 1, nextColumnIdx, m)) % self.MOD

        self.t[remainingCols][prevColumnIdx] = totalWays
        return totalWays

    def colorTheGrid(self, m: int, n: int) -> int:
        self.columnStates = []
        self.generateColumnStates("", m, '#')

        patternCount = len(self.columnStates)
        self.t = [[-1] * patternCount for _ in range(n)]

        result = 0
        for i in range(patternCount):
            result = (result + self.solve(n - 1, i, m)) % self.MOD

        return result
