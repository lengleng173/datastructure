# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def dfs(node_l,node_r):
            if node_l is None and node_r is None:
                return True
            if node_l is None or node_r is None:
                return False
            if node_l.val!=node_r.val:return False
            return dfs(node_l.left,node_r.right) and dfs(node_l.right,node_r.left)
        return dfs(root.left,root.right)