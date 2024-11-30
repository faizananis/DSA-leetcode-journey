from collections import defaultdict, deque

class Solution:
    def __init__(self):
        self.adj = defaultdict(list)
        self.in_degree = defaultdict(int)
        self.out_degree = defaultdict(int)

    def get_start_node(self):
        start_node = None
        for node in self.out_degree:
            if self.out_degree[node] - self.in_degree[node] == 1:
                return node  # Euler path exists but not Euler Circuit
            if self.out_degree[node] > 0:
                start_node = node
        return start_node  # Euler circuit or Euler path both exist

    def get_eulerian_path(self, curr, eulerian_path):
        while self.out_degree[curr] > 0:
            self.out_degree[curr] -= 1
            next_node = self.adj[curr][self.out_degree[curr]]
            self.get_eulerian_path(next_node, eulerian_path)
        eulerian_path.append(curr)

    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        for from_node, to_node in pairs:
            self.adj[from_node].append(to_node)
            self.out_degree[from_node] += 1
            self.in_degree[to_node] += 1

        start_node = self.get_start_node()  # Eulerian path is guaranteed in this problem

        eulerian_path = []
        self.get_eulerian_path(start_node, eulerian_path)

        res = []
        for i in range(len(eulerian_path) - 1, 0, -1):
            res.append([eulerian_path[i], eulerian_path[i - 1]])
        return res
        