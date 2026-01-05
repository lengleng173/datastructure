# 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
# 输入：root = [4,2,7,1,3,6,9]
# 输出：[4,7,2,9,6,3,1]


class TreeNode:
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None

def createBinaryTree(nums):
    if not nums:
        return None
    
    def helper(index):
        if index>=len(nums) or nums[index] is None:
            return None
        node=TreeNode(nums[index])
        node.left=helper(2*index)
        node.right=helper(2*index+1)
        return node
    root=helper(1)
    return root

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        from collections import deque
        if not root:  # 先检查根节点是否为空
            return None
        queue=deque()
        queue.append(root)
        while queue:
            node=queue.popleft()
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
            node.left,node.right=node.right,node.left
        return root
    
    #优化,直接递归左右孩子
    # class Solution:
    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     if not root:
    #         return root
    #     root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    #     return root
            
nums = [4,2,7,1,3,6,9]
root=createBinaryTree(nums)
so=Solution()
print(so.invertTree(root))