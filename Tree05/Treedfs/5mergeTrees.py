# 给你两棵二叉树： root1 和 root2 。

# 想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。你需要将这两棵树合并成一棵新二叉树。合并的规则是：如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；否则，不为 null 的节点将直接作为新二叉树的节点。

# 返回合并后的二叉树。

# 注意: 合并过程必须从两个树的根节点开始。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        root=TreeNode()
        def dfs(node,node1,node2):
            if node1 is None and node2 is None:
                return None
            if node1 and node2:
                node=TreeNode()
                node.val=node1.val+node2.val
                if node1.left or node2.left:
                    node.left=dfs(node.left,node1.left,node2.left)
                if node1.right or node2.right:
                    node.right=dfs(node.right,node1.right,node2.right)
                return node
            elif node1:
                return node1
            elif node2:
                return node2
        return dfs(root,root1,root2)
