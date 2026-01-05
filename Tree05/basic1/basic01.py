#定义二叉树
class TreeNode:
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None
    
#创建二叉树(依据数组)
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

nums=[None,1,2,3,4,5,6,7,8,9,None,11,None,None,14,15,16,17]
root=createBinaryTree(nums)
print(root.left.left.val)