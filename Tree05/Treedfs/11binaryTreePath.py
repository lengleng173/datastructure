# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path=[]
        def dfs(node,tmp):
            if node is None:
                return
            if node.left is None and node.right is None:
                tmp+=str(node.val)
                tmp='->'.join(tmp.split(','))
                path.append(tmp)
                return 
            tmp=tmp+str(node.val)+','
            if node.left:dfs(node.left,tmp)
            if node.right:dfs(node.right,tmp)
        dfs(root,'')
        return path
    
        # def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # ans = []
        # def dfs(node, last_str):
        #     if node is None:
        #         return
        #     last_str.append(str(node.val))
        #     if node.left is None and node.right is None:
        #         ans.append("->".join(last_str))

        #     dfs(node.left, last_str)
        #     dfs(node.right, last_str)
        #     last_str.pop()

        # dfs(root, [])
        # return ans