def search(nums,left,right,target):
    if left==right:
        return left if nums[left]==target else -1
    mid=(left+right)//2
    if nums[mid]>target:
        return search(nums,left,mid-1,target)
    if nums[mid]<target:
        return search(nums,mid+1,right,target)
    return mid

print(search([-1,0,3,5,9,12],0,5,12))