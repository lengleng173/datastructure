
def quicksort(l,left,right,k):
    if left<right:
        part=partition(l,left,right)
        quicksort(l,left,part-1,k)
        quicksort(l,part+1,right,k)
    return (l[:k]if len(l)>k else l)
def partition(l,left,right):
    index=left+1
    for i in range(left,right):
        if l[left]>l[i]:
            l[index],l[i]=l[i],l[index]
            index+=1
    l[index-1],l[left]=l[left],l[index-1]
    return index-1
arr=[0,1,2,1]
k=1
print(quicksort(arr,0,len(arr),k))