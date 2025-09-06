class Solution:
    def solve(self, l: int, r: int) -> int:
        L = 1        # starting left bound
        S = 1        # step count
        steps = 0

        while L <= r:
            R = 4 * L - 1   # right bound of this range

            # overlap with [l, r]
            start = max(L, l)
            end = min(R, r)

            if start <= end:
                steps += (end - start + 1) * S

            # move to next block
            S += 1
            L *= 4

        return steps

    def minOperations(self, queries: List[List[int]]) -> int:
        result = 0
        for l, r in queries:
            steps = self.solve(l, r)
            result += (steps + 1) // 2   # divide by 2, round up
        return result

        