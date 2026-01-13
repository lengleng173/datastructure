# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,cnt):
            if node is None:
                return False
            cnt+=node.val
            if node.left is None and node.right is None:
                return (cnt==targetSum)
            return dfs(node.left,cnt) or dfs(node.right,cnt)
        return dfs(root,0)