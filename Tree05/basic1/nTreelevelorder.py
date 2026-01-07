# 给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。

# 树的序列化输入是用层序遍历，每组子节点都由 null 值分隔（参见示例）。
# 输入：root = [1,null,3,2,4,null,5,6]
# 输出：[[1],[3,2,4],[5,6]]
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return  []
        queue=deque()
        queue.append(root)
        res=[]
        size=1
        while queue:
            part=[]
            length=0
            for i in range(size):
                node=queue.popleft()
                part.append(node.val)
                length+=len(node.children)
                queue.extend(node.children)
            size=length
            res.append(part)
        return res