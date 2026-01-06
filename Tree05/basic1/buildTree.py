# 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
# 输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# 输出: [3,9,20,null,null,15,7]

class TreeNode:
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None
from typing import List
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) ==0 or len(inorder) ==0:
            return None
        root=TreeNode()
        for i in preorder:
            root.val=i
            try:
                idx=inorder.index(i)
                root.left=self.buildTree(preorder[1:],inorder[:idx])
                root.right=self.buildTree(preorder[1:],inorder[idx+1:])
                return root
            except:
                continue

#优化后
        # def recur(root,left,right):
        #     if left>right:#递归终止
        #         return 
        #     node=TreeNode(preorder[root])
        #     i=dic[preorder[root]]
        #     node.left=recur(root+1,left,i-1)
        #     node.right=recur(root+i-left+1,i+1,right)
        #     return node#回溯
        # dic={}
        # for i in range(len(inorder)):
        #     dic[inorder[i]]=i
        # return recur(0,0,len(inorder)-1)
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
so=Solution()
root=so.buildTree(preorder,inorder)

