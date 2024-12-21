class Solution:
    def dfs(self, adj, values, k, count, curr, parent=-1):
        total_sum = values[curr]
        for nbr in adj[curr]:
            if nbr != parent:
                total_sum += self.dfs(adj, values, k, count, nbr, curr)
        total_sum %= k
        if total_sum == 0:
            count[0] += 1
        return total_sum

    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        from collections import defaultdict
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        count = [0]
        self.dfs(adj, values, k, count, 0)
        return count[0]
    
        