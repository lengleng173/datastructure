# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cnt=0
        def dfs(root):
            nonlocal cnt
            if root is None:
                return None
            if root.right:dfs(root.right)
            cnt+=root.val
            root.val=cnt
            if root.left:dfs(root.left)

        dfs(root)
        return root