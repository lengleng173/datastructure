# 700给定二叉搜索树（BST）的根节点 root 和一个整数值 val。

# 你需要在 BST 中找到节点值等于 val 的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 null 。
# 输入：root = [4,2,7,1,3], val = 2
# 输出：[2,1,3]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None :
            return None
        if root.val==val:
            return root
        if root.val>val:return self.searchBST(root.left,val)
        if root.val<val:return self.searchBST(root.right,val)