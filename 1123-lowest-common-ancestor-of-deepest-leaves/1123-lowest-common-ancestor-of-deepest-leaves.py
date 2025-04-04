# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLCA(self, curr):
        if not curr:
            return (None, 0)
        
        left_node, left_depth = self.findLCA(curr.left)
        right_node, right_depth = self.findLCA(curr.right)
        
        if left_depth == right_depth:
            return (curr, 1 + left_depth)
        elif left_depth > right_depth:
            return (left_node, 1 + left_depth)
        else:
            return (right_node, 1 + right_depth)
    
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        res_node, res_depth = self.findLCA(root)
        return res_node

        