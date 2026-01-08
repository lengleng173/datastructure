# 给定一个二叉树，找出其最小深度。

# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

# 说明：叶子节点是指没有子节点的节点。

# 输入：root = [3,9,20,null,null,15,7]
# 输出：2
# 示例 2：

# 输入：root = [2,null,3,null,4,null,5,null,6]
# 输出：5

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional,List
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        def dfs(node,depth):
            min_depth=200000
            if node.left is None and node.right is None:
                return depth
            if node.left:min_depth=min(dfs(node.left,depth+1),min_depth)
            if node.right:min_depth=min(dfs(node.right,depth+1),min_depth)
            return min_depth
        return dfs(root,1)