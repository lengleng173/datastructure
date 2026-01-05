#先序中序后序都属于dfs，层次遍历属于bfs


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

#先序遍历dfs（使用递归）
def preordertraversal(root):
    if root is None:
        return []
    preorderres.append(root.val)
    preordertraversal(root.left)
    preordertraversal(root.right)

#中序遍历
def inordertraversal(root):
    if root is None:
        return []
    inordertraversal(root.left)
    inorderres.append(root.val)
    inordertraversal(root.right)

#后序遍历
def postordertraversal(root):
    if root is None:
        return []
    postordertraversal(root.right)
    postordertraversal(root.left)
    postorderres.append(root.val)

#层次遍历bfs（使用queue）
from collections import deque
def levelorder(root):
    if root is None:
        return []
    queue=deque()
    res=[]
    queue.append(root)
    while queue:
        node=queue.popleft()
        res.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return res
###层次遍历+层数-》利用每层len或者i
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         queue=deque()
#         res=[]
#         if root is None:
#             return []
#         queue.append(root)
#         while queue:
#             tmp=[]
#             size=len(queue)
#             for _ in range(size):
#                 node=queue.popleft()
#                 tmp.append(node.val)
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             res.append(tmp)
#         return res
preorderres=[]
inorderres=[]
postorderres=[]
nums=[None,1,2,3,4,5,6,7,8,9,None,11,None,None,14,15,16,17]
root=createBinaryTree(nums)
print('-------先序遍历结果为-------')
preordertraversal(root)
print(preorderres)
print('-------中序遍历结果为-------')
inordertraversal(root)
print(inorderres)
print('-------后序遍历结果为-------')
postordertraversal(root)
print(postorderres)
print('-------层次遍历结果为-------')
print(levelorder(root))