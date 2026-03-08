class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeList(arr,left,right):
    if len(arr)==0:return None
    if left>=right:
        return arr[left]
    mid=(left+right)//2
    return merge(mergeList(arr,left,mid), mergeList(arr,mid+1,right))

def merge(l,r):
    new=ListNode()
    n=new
    while l and r:
        if l.val>=r.val:
            n.next=ListNode(r.val)
            n=n.next
            r=r.next
        else:
            n.next=ListNode(l.val)
            n=n.next
            l=l.next
    if l:n.next=l
    if r:n.next=r
    return new.next

lists=[]
arry=[]
for i in lists:
    h=ListNode()
    q=h
    for i in i:
        q.next=ListNode(i)
        q=q.next
    arry.append(h.next)
h=mergeList(arry,0,len(arry)-1)
print("排序后的链表:")
while h:
    print(h.val, end=" ")
    h = h.next