# 给定一个单链表，请设定一个函数，将链表的奇数位节点和偶数位节点分别放在一起，重排后输出。
# 注意是节点的编号而非节点的数值。


# 示例1
# 输入：
# {1,2,3,4,5,6}
# 复制
# 返回值：
# {1,3,5,2,4,6}
# 复制
# 说明：
# 1->2->3->4->5->6->NULL
# 重排后为
# 1->3->5->2->4->6->NULL
   
class Solution:
    def oddEvenList(self , head: ListNode) -> ListNode:
        # write code here
        if head == None or head.next == None:
            return head
        odd, even = head, head.next
        preodd, preeven = odd, even
        while even and even.next:
            odd.next = even.next
            odd=odd.next
            even.next = odd.next
            even=even.next

        odd.next = preeven
        return head
        
        