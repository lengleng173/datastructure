# 实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。

# 注意：本题相对原题稍作改动

# 示例：

# 输入： 1->2->3->4->5 和 k = 2
# 输出： 4
# 说明：

# 给定的 k 保证是有效的。

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def kthToLast(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: int
        """
        pre=ListNode(0,head)
        fast=slow=pre
        for i in range(k):
            fast=fast.next
        while fast:
            fast=fast.next
            slow=slow.next
        return slow.val