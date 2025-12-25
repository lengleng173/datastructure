# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists( list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    p=ListNode()
    c=p
    while list1 and list2:
        x=list1.val
        y=list2.val
        if x<=y :
            c.next=ListNode(list1.val)
            list1=list1.next
            
        else:
            c.next=ListNode(list2.val)
            list2=list2.next

    c.next=list1 if list1 is not None else list2
    return p.next    

l1=[1,2,4]
l2=[1,3,4]
list1=ListNode(-1)
p=list1
for i in l1:
    p.val=i
    p=p.next
list2=ListNode()
p=list2
for i in l2:
    p.val=i
    p=p.next
list3=mergeTwoLists(list1,list2)
while list3:
    print(list3.val)
    list3=list3.next