# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre_idx = 0
        self.post_idx = 0

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        curr = TreeNode(preorder[self.pre_idx])
        self.pre_idx += 1

        if curr.val != postorder[self.post_idx]:
            curr.left = self.constructFromPrePost(preorder, postorder)
        if curr.val != postorder[self.post_idx]:
            curr.right = self.constructFromPrePost(preorder, postorder)

        self.post_idx += 1
        return curr

        # my_set=set()
        # pre=0
        # post=0
        # node=TreeNode(preorder[0])
        # def backtrack(treeNode):
        #     if preorder[pre]==postorder[post]:
        #         return
        #     pre+=1
        #     treeNode.left=TreeNode(preorder[pre])
        #     my_set.add(preorder[pre])
        #     backtrack(treeNode.left)
        #     if postorder[post] not in my_set:
        #         treeNode.right=TreeNode(postorder[post])
        #     post+=1
        #     if postorder[post] not in my_set:
        #         backtrack(treeNode.right)
        # return backtrack(node)