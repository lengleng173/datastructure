# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q=deque()
        q.append(root)
        size=0
        while q:
            size+=len(q)
            for _ in range(len(q)):
                node=q.popleft()
                if node.left:q.append(node.left)
                if node.right:q.append(node.right)
        return size
    
#完全二叉树解法
        # if not root: return 0
        # level = 1
        # left, right = root.left, root.right
        # # 找到树中最左和最右节点
        # while left and right:
        #     level += 1
        #     left, right = left.left, right.right
        # # 从左右点判断是否是完美二叉树，只有一个节点也是完美二叉树，1，3，7 都是完美二叉树
        # if not left and not right:
        #     return 2**level - 1 
        # # 不是完美二叉树则继续算他的子树（顶点+左右子树）
        # return 1+self.countNodes(root.left)+self.countNodes(root.right)