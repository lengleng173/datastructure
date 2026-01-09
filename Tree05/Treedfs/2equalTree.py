# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node_p,node_q,depth):
            if node_p is None and node_q is None:
                return True
            elif (node_p is None and node_q) or (node_p and node_q is None):
                return False
            if node_p.val!=node_q.val:
                return False
            if not dfs(node_p.left,node_q.left,depth+1):return False
            if not dfs(node_p.right,node_q.right,depth+1):return False
            return True
        return dfs(p,q,0)