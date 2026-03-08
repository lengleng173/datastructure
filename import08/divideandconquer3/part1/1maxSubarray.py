def maxSubArray(x,left,right):
    if left==right:
        return x[left]
    mid=(left+right)//2
    a=maxSubArray(x,left,mid)
    b=maxSubArray(x,mid+1,right)
    passmid=cross(x,left,mid,right)
    return max(a,b,passmid)

def cross(x,left,mid,right):
    suml=x[mid]
    ml=x[mid]
    for i in range(mid-1,left,-1):
        suml+=x[i]
        if suml>ml:ml=suml
    suml=ml 
    for i in range(mid+1,right,1):
        suml+=x[i]
        if suml>ml:ml=suml
    return  ml   
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4],0,8))