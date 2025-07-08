class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()  # Sort events by start time

        n = len(events)
        starts = [event[0] for event in events]  # For binary search

        @lru_cache(maxsize=None)
        def solve(i, remaining_k):
            if remaining_k == 0 or i >= n:
                return 0

            # Event details
            start, end, value = events[i]

            # Binary search to find the next non-overlapping event
            next_index = bisect_right(starts, end)

            # Two options:
            take = value + solve(next_index, remaining_k - 1)
            skip = solve(i + 1, remaining_k)

            return max(take, skip)

        return solve(0, k)