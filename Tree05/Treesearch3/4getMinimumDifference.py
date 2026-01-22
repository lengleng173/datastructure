# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。

# 差值是一个正数，其数值等于两值之差的绝对值。
# 输入：root = [4,2,6,1,3]
# 输出：1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        global mini
        if root is None:
            return None
        left=1000000000
        right=1000000000
        if root.left:
            node=root.left
            while node.left:node=node.right
            left=root.val-node.val 
            left=min(left,self.getMinimumDifference(root.left))
        if root.right:
            node=root.right
            while node.right:node=node.left
            right=node.val-root.val
            right=min(right,self.getMinimumDifference(root.right))
        mini=min(left,right)
        return mini
    
#！二叉树的中序遍历就是顺序排序了

class Solution:
    pre=-10000000
    mini=10000000
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        global pre,mini
        if root is None:
            return None
        if root.left:self.getMinimumDifference(root.left)
        mini=min((root.val-pre),mini)
        pre=root.val
        if root.right:self.getMinimumDifference(root.right)
        return mini