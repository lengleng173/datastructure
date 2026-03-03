def mergesort(l,left,right):
    
    if right>left:
        mid=(right+left)//2
        mergesort(l,left,mid)
        mergesort(l,mid+1,right)
        merge(l,left,mid,right)
def merge(l,left,mid,right):
    tmp=[]
    lpoint,rpoint=left,mid+1
    while lpoint<=mid and rpoint<=right:
        if l[lpoint]<l[rpoint]:
            tmp.append(l[lpoint])
            lpoint+=1
        else:
            tmp.append(l[rpoint])
            rpoint+=1
    if lpoint<=mid:
        tmp.extend(l[lpoint:mid+1])
    if rpoint<right:
        tmp.extend(l[rpoint:right+1])
    for i in range(len(tmp)):
        l[i+left]=tmp[i]

l=[35,63,48,9,86,24,53,11]
mergesort(l,0,len(l)-1)
print(l)