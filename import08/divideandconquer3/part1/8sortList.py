class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def sortList(head):
    if head is None or head.next is None:
        return head
    fast,slow=head,head
    pre = None
    while fast and fast.next:
        fast=fast.next.next
        pre=slow
        slow=slow.next
    pre.next=None
    #合并并排序
    return merge(sortList(head),sortList(slow))
def merge(head,slow):
    
    new=ListNode()
    newpoint=new
    while head and slow:
        if head.val>slow.val:
            newpoint.next=ListNode(slow.val)
            slow=slow.next
            newpoint=newpoint.next
        else:
            newpoint.next=ListNode(head.val)
            head=head.next
            newpoint=newpoint.next
    if head:newpoint.next=head
    if slow:newpoint.next=slow
    return new.next
head = [4,2,1,3]
h=ListNode()
q=h
for i in head:
    q.next=ListNode(i)
    q=q.next

p=sortList(h.next)
print("排序后的链表:")
while p:
    print(p.val, end=" ")
    p = p.next
print()  # 换行