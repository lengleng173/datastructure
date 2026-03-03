l=[35,63,48,9,86,24,53,11]
def quicksort(l,left,right):
    if left<right:
        part=partition(l,left,right)
        quicksort(l,left,part-1)
        quicksort(l,part+1,right)
def partition(l,left,right):
    index=left+1
    for i in range(left,right):
        if l[left]>l[i]:
            l[index],l[i]=l[i],l[index]
            index+=1
    l[index-1],l[left]=l[left],l[index-1]
    return index-1
quicksort(l,0,len(l)-1)
print(l)