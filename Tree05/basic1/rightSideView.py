# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue=deque()
        queue.append(root)
        res=[root.val]
        while queue:
            for i in range(len(queue)):
                node=queue.popleft()
                if node.left :
                    queue.append(node.left)
                if node.right :
                    queue.append(node.right)
            if queue:res.append(queue[-1].val)
        return res
    
    #dfs解法
# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         ans=[]
#         depth=0
#         def dfs(root,depth):
#             if root is None:
#                 return
#             if depth==len(ans):
#                 ans.append(root.val)
#             dfs(root.right,depth+1)
#             dfs(root.left,depth+1)    
#         dfs(root,0)
#         return ans