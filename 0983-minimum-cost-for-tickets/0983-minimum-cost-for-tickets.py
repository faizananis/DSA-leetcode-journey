class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)

        @lru_cache(None)
        def solve(pos, reachability):
            if pos >= n:
                return 0
            if reachability >= days[pos]:
                return solve(pos + 1, reachability)

            one = costs[0] + solve(pos + 1, days[pos])
            seven = costs[1] + solve(pos + 1, days[pos] + 6)
            month = costs[2] + solve(pos + 1, days[pos] + 29)

            return min(one, seven, month)

        return min(
            costs[0] + solve(0, days[0]),
            costs[1] + solve(0, days[0] + 6),
            costs[2] + solve(0, days[0] + 29),
        )