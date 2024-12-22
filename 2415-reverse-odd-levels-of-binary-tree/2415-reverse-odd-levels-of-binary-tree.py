# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        level = 0

        while q:
            size = len(q)
            level_nodes = []

            for _ in range(size):
                curr = q.popleft()
                level_nodes.append(curr)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            if level % 2 == 1:
                n = len(level_nodes)
                for j in range(n // 2):
                    level_nodes[j].val, level_nodes[n - j - 1].val = level_nodes[n - j - 1].val, level_nodes[j].val

            level += 1

        return root
