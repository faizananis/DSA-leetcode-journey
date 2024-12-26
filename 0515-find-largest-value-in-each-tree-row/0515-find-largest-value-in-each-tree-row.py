# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        queue=deque()
        largest=-2**31-1 #-("inf")
        if root:
            queue.append(root)
        while queue:
            largest=-2**31-1
            for _ in range(len(queue)):
                if queue:
                    node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                largest=max(largest,node.val)
            ans.append(largest)
        return ans
