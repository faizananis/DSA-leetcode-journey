class Solution:
     def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7

        # Make Adjacency List
        adj = [[] for _ in range(n)]
        for road in roads:
            adj[road[0]].append((road[1], road[2]))
            adj[road[1]].append((road[0], road[2]))

        # Apply Dijkstra and keep tracking number of ways to reach a node with min_cost
        minheap = []
        heapq.heappush(minheap, (0, 0))  # (cost, node): Source is 0
        processed = [False] * n

        count_ways = [0] * n  # Count total ways to reach a node from start (0)
        count_ways[0] = 1  # There is 1 way to reach the start node
        min_cost = [float('inf')] * n
        min_cost[0] = 0  # Initialize min_cost for the source node

        while minheap:
            cost, curr_node = heapq.heappop(minheap)

            if processed[curr_node]:
                continue
            processed[curr_node] = True

            for nbr, weight in adj[curr_node]:
                if not processed[nbr]:
                    if cost + weight == min_cost[nbr]:
                        # Found another shortest path
                        count_ways[nbr] = (count_ways[nbr] + count_ways[curr_node]) % MOD
                    elif cost + weight < min_cost[nbr]:
                        # Found a shorter path
                        min_cost[nbr] = cost + weight
                        count_ways[nbr] = count_ways[curr_node]
                        heapq.heappush(minheap, (min_cost[nbr], nbr))

        return count_ways[n - 1]