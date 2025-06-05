class Solution:
    def dfs(self, adj, curr, visited):
        visited[ord(curr) - ord('a')] = 1
        min_char = curr

        for neighbor in adj[curr]:
            if not visited[ord(neighbor) - ord('a')]:
                result = self.dfs(adj, neighbor, visited)
                min_char = min(min_char, result)

        return min_char

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        adj = defaultdict(list)
        n = len(s1)

        # Build adjacency list
        for i in range(n):
            u = s1[i]
            v = s2[i]
            adj[u].append(v)
            adj[v].append(u)

        result = []

        for ch in baseStr:
            visited = [0] * 26
            result.append(self.dfs(adj, ch, visited))

        return ''.join(result)