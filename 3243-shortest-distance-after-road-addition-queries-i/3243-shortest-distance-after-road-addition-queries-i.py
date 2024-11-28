from collections import deque

class Solution:
    def shortestPath(self, adj, n):
        queue = deque([0])
        visited = [False] * n
        visited[0] = True
        distance = 0

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == n - 1:
                    return distance
                for neighbor in adj[curr]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            distance += 1
        return -1  # If there is no path to the last node
        
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for i in range(n - 1):
            adj[i].append(i + 1)

        result = []
        for query in queries:
            adj[query[0]].append(query[1])
            result.append(self.shortestPath(adj, n))
        return result