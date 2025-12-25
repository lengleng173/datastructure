nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
m=int(input())
a=nums1[:m]
def merge(a,b):
    c=[]
    while len(a)!=0 and len(b)!=0:
        if a[0]<b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))

    c.extend(a)
    c.extend(b)
    return c

nums1=(merge(a,nums2))
print(nums1)