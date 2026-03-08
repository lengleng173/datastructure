class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def CMB(nums,left,right):
            if left==right:
                return None
            root=TreeNode()
            mm=root.val=max(nums[left:right])
            mid=nums.index(mm)
            root.left=CMB(nums,left,mid)
            root.right=CMB(nums,mid+1,right)
            return root
        return CMB(nums,0,len(nums))