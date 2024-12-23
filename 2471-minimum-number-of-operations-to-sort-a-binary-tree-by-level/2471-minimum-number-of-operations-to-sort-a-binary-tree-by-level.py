# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMinSwaps(self, values):
        n = len(values)
        min_swaps = 0

        # Map value -> original index
        value_to_index = {value: i for i, value in enumerate(values)}

        # Sort values to get the expected positions
        sorted_values = sorted(values)
        visited = [False] * n

        for i in range(n):
            if visited[i] or value_to_index[sorted_values[i]] == i:
                continue

            # Find the cycle length
            cycle_length = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = value_to_index[sorted_values[j]]
                cycle_length += 1

            min_swaps += cycle_length - 1

        return min_swaps

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        min_swaps = 0

        while queue:
            size = len(queue)
            values = []

            for _ in range(size):
                curr = queue.popleft()
                values.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            min_swaps += self.findMinSwaps(values)

        return min_swaps
        