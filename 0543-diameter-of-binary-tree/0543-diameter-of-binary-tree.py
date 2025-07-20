# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_diameter = 0  # This will hold the final answer

        def dfs(node):
            if not node:
                return 0  # Base case: depth of null node is 0

            # Recursively find the depth of left and right subtrees
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            # Update the diameter if this path is longer
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)

            # Return the depth of the current node
            return 1 + max(left_depth, right_depth)

        dfs(root)
        return self.max_diameter

        