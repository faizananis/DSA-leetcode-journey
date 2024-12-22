class Solution:
    def __init__(self):
        self.segTree = []  # Segment Tree

    def buildSegmentTree(self, heights, start, end, st_idx):
        if start == end:
            self.segTree[st_idx] = start
            return

        mid = start + (end - start) // 2
        self.buildSegmentTree(heights, start, mid, 2 * st_idx)
        self.buildSegmentTree(heights, mid + 1, end, 2 * st_idx + 1)

        self.segTree[st_idx] = (self.segTree[2 * st_idx]
        if heights[self.segTree[2 * st_idx]] >= heights[self.segTree[2 * st_idx + 1]]
        else self.segTree[2 * st_idx + 1])

    def rangeMaxQuery(self, heights, qs, qe, start, end, st_idx=1):
        if start >= qs and end <= qe:  # Total Overlap
            return self.segTree[st_idx]
        if start > qe or end < qs:  # No Overlap
            return float('-inf')

        # Partial Overlap
        mid = start + (end - start) // 2
        left_max = self.rangeMaxQuery(heights, qs, qe, start, mid, 2 * st_idx)
        right_max = self.rangeMaxQuery(heights, qs, qe, mid + 1, end, 2 * st_idx + 1)

        if left_max == float('-inf'):
            return right_max
        if right_max == float('-inf'):
            return left_max

        return left_max if heights[left_max] >= heights[right_max] else right_max

    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        self.segTree = [0] * (4 * n + 1)
        st_idx = 1  # Segment Tree Index: Root at index 1

        self.buildSegmentTree(heights, 0, n - 1, st_idx)

        res = []
        for query in queries:
            alice = min(query[0], query[1])
            bob = max(query[0], query[1])

            if alice == bob or heights[bob] > heights[alice]:
                res.append(bob)
                continue

            # Binary Search + RMQ (Range Max Query)
            low, high, ans = bob, n - 1, float('inf')
            while low <= high:
                mid = low + (high - low) // 2
                rmq = self.rangeMaxQuery(heights, low, mid, 0, n - 1, st_idx)

                if heights[rmq] > heights[alice]:
                    high = mid - 1
                    ans = min(ans, rmq)
                else:
                    low = mid + 1

            res.append(-1 if ans == float('inf') else ans)
        return res
    
        