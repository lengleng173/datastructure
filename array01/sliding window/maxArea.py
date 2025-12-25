def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    left=0
    right=len(height)-1
    max_val=min(height[-1],height[0])*(len(height)-1)
    while left<right :
        if height[left]<height[right]:#左边矮
            prf=left
            while height[prf]<=height[left] and prf<len(height):
                prf+=1
            left=prf
            val=(right-left)*min(height[left],height[right])#越界也没事，变成负数了
        else:#右边矮
            prr=right
            while height[prr]<=height[right] and prr>0:
                prr-=1
            right=prr
            val=(right-left)*min(height[left],height[right])#越界也没事，变成负数了
        max_val=max(val,max_val)
    return max_val

height=[1,2,4,3]
print(maxArea(height))