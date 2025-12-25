# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。

# 图示两个链表在节点 c1 开始相交：
# 题目数据 保证 整个链式结构中不存在环。

# 注意，函数返回结果后，链表必须 保持其原始结构 。

# 自定义评测：

# 评测系统 的输入如下（你设计的程序 不适用 此输入）：

# intersectVal - 相交的起始节点的值。如果不存在相交节点，这一值为 0
# listA - 第一个链表
# listB - 第二个链表
# skipA - 在 listA 中（从头节点开始）跳到交叉节点的节点数
# s
# kipB - 在 listB 中（从头节点开始）跳到交叉节点的节点数
# 评测系统将根据这些输入创建链式数据结构，并将两个头节点 headA 和 headB 传递给你的程序。如果程序能够正确返回相交节点，那么你的解决方案将被 视作正确答案 。

#  输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# 输出：Intersected at '8'
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a=set()
        p,q=headA,headB
        while q:
            a.add(q)
            q=q.next
        while p:
            if p in a:
                return p
            p=p.next
        return None
    #指针走两遍，都走前面不同部分
    # class Solution:
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    #     if not headA or not headB:
    #         return None
            
    #     pA, pB = headA, headB
        
    #     while pA != pB:
    #         # 如果pA走到末尾，就指向headB继续走
    #         if pA:
    #             pA = pA.next
    #         else:
    #             pA = headB
    #         # pA = pA.next if pA else headB
    #         # 如果pB走到末尾，就指向headA继续走
    #         pB = pB.next if pB else headA
            
    #     # 循环结束时，pA和pB要么指向相交节点，要么都是None
    #     return pA  
# pA路径: A独有 → 公共 → B独有 → 公共
# pB路径: B独有 → 公共 → A独有 → 公共