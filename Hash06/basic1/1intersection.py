# 给定两个数组 nums1 和 nums2 ，返回 它们的 交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。

# 示例 1：

# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2]
# 示例 2：

# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[9,4]
# 解释：[4,9] 也是可通过的

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=dict()
        b=dict()
        for i in nums1:
            a[i]=1
        for i in nums2:
            b[i]=1
        path=[]
        for i in a.keys():
            if i in b.keys():
                path.append(i)

        return path
    
    #return list(set(nums1)&set(nums2))集合与 Python 中求两个集合交