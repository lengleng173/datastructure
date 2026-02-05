l=[20,413,3,53,90,324]
def quicksort(l):
    if len(l)==0 or len(l)==1:
        return l
    a=l[0]
    left=[]
    right=[]
    for i in l[1:]:
        if i<a:
            left.append(i)
        else:
            right.append(i)
    left=quicksort(left)
    right=quicksort(right)
    left.append(a)
    left.extend(right)
    return left
print(quicksort(l))