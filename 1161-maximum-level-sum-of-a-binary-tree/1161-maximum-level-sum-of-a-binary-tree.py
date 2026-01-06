# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maximum=(root.val,1)
        deq=deque()
        deq.append(root)
        i=1
        while deq:
            sums=0
            for _ in range(len(deq)):
                node=deq.popleft()
                sums+=node.val
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
            if sums>maximum[0]:
                maximum=(sums,i)
            i+=1
        return maximum[1]
