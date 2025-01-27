class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        INT_MAX = 10000
        dist = [[INT_MAX] * numCourses for _ in range(numCourses)]
        
        # Initialize distance matrix
        for i in range(numCourses):
            dist[i][i] = 0  # No self-loop
        
        # Populate adjacency and distance matrix
        for edge in prerequisites:
            dist[edge[0]][edge[1]] = 1
        
        # Floyd-Warshall Algorithm
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if dist[i][k] != INT_MAX and dist[k][j] != INT_MAX and dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Answer queries
        ans = []
        for query in queries:
            ans.append(dist[query[0]][query[1]] < INT_MAX)
        return ans
