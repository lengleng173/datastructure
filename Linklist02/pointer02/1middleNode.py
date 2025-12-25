# 876给你单链表的头结点 head ，请你找出并返回链表的中间结点。

# 如果有两个中间结点，则返回第二个中间结点。
# 输入：head = [1,2,3,4,5]
# 输出：[3,4,5]
# 解释：链表只有一个中间结点，值为 3 。

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        fast,slow=head,head
        while fast!=None and fast.next!=None:
            fast=fast.next.next
            slow=slow.next
        return slow
head = None
for i in [5,4,3,2,1,0]:
    head = ListNode(i,head)
solution = Solution()
result = solution.middleNode(head)
print(f"中间节点的值: {result.val}") 