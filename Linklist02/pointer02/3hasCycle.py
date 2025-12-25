# 142给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

# 不允许修改 链表。
# 输入：head = [3,2,0,-4], pos = 1
# 输出：返回索引为 1 的链表节点
# 解释：链表中有一个环，其尾部连接到第二个节点

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        a=set()
        a.add(head)
        if head==None or head.next==None:
            return None
        p=head.next
        while p:
            if p in a:
                return p
            a.add(p)
            p=p.next
        return None
    
    #快慢指针，终会相遇
    # class Solution(object):
    # def detectCycle(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     if not head or not head.next:
    #         return None
            
    #     # 第一阶段：判断是否有环
    #     slow = fast = head
    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next
    #         if slow == fast:  # 有环，相遇了
    #             # 第二阶段：找环的入口
    #             p1 = head
    #             p2 = slow  # 或者 fast，此时两者相等
    #             while p1 != p2:
    #                 p1 = p1.next
    #                 p2 = p2.next
    #             return p1
        
    #     return None  # 无环