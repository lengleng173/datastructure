# 给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。
# 输入: root = [1,3,2,5,3,null,9]
# 输出: [1,3,9]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional,List
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue=deque()
        queue.append(root)
        res=[]
        while queue:
            max_floor=float('-inf')#表示负无穷
            for _ in range(len(queue)):
                node=queue.popleft()
                max_floor=max(node.val,max_floor)
                if node.left:queue.append(node.left)
                if node.right:queue.append(node.right)
            res.append(max_floor)
        return res