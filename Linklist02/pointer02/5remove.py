#19给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        slow,fast=head,head
        
        for i in range(n):
            fast=fast.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next

        if slow.next==None:
            return None
        if fast==None:
            return head.next
        slow.next=slow.next.next
        return head

