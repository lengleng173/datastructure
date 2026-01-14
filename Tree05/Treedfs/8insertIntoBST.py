# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node=root
        if node is None:
            return TreeNode(val)
        while node:
            if val<node.val:
                if node.left:
                    node=node.left
                else:
                    new_node=TreeNode(val)
                    node.left=new_node
                    break
            elif val>node.val:
                if node.right:
                    node=node.right
                else:
                    new_node=TreeNode(val)
                    node.right=new_node
                    break
        return 
    


# class Solution:
#     def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         node=root
#         if node is None:
#             return TreeNode(val)
#         while node:
#             if val<node.val:
#                 if node.left:
#                     node=node.left
#                 else:
#                     new_node=TreeNode(val)
#                     node.left=new_node
#                     break
#             elif val>node.val:
#                 if node.right:
#                     node=node.right
#                 else:
#                     new_node=TreeNode(val)
#                     node.right=new_node
#                     break
#         return root