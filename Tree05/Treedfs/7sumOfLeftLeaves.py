# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        cnt_l=0
        def dfs(node,flag):
            nonlocal cnt_l
            if node is None:
                return 
            if node.left is None and node.right is None and flag:
                cnt_l+=node.val
            dfs(node.left,True)
            dfs(node.right,False)
        dfs(root,False)
        return cnt_l