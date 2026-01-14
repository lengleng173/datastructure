"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
from typing import Optional

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(node):
            if node is None or node.left is None:
                return None
            if node.left:node.left.next=node.right
            if node.next:node.right.next=node.next.left
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return root
    
    # -----bfs
    # class Solution:
    # def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
    #     if not root:
    #         return root

    #     queue=collections.deque([root])

    #     while queue:
    #         n=len(queue)
    #         pre=None
    #         for i in range(n):
    #             cur=queue.popleft()
    #             if pre:
    #                 pre.next=cur
    #             pre=cur
    #             if pre.left:
    #                 queue.append(pre.left)
    #             if pre.right:
    #                 queue.append(pre.right)

    #     return root
                    