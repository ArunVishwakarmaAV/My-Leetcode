# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.res=0
        def bfs(node):
            if node == None:
                return 0
            l=bfs(node.left)
            r=bfs(node.right)
            self.res+=abs(l-r)
            return l+r+node.val
        bfs(root)
        return self.res
        