def searchMatrix( matrix, target):
    top=0
    right=len(matrix[0])-1
    while top<len(matrix) and right>=0:
        if matrix[top][right]>target:
            right-=1
        elif matrix[top][right]<target:
            top+=1
        else:
            return True
    return False
