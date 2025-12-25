def findDiagonalOrder(mat):
    top=0
    left=0
    dir=1
    c=[]
    sums=0
    while top<len(mat) and left<len(mat[0]) :
        c.append(mat[top][left])
        top-=dir
        left+=dir
        if top<0:
            dir*=-1
            top+=1
            if left>=len(mat[0]):
                top+=1
                left-=1
            
        elif left<0:
            dir*=-1
            left+=1
            if top>=len(mat):
                top-=1
                left+=1

        elif top>=len(mat):
            dir*=-1
            top-=1
            left+=2
        elif left>=len(mat[0]):
            dir*=-1
            top+=2
            left-=1   
    return c


mat=[[1,2,3],[4,5,6],[7,8,9]]
print(findDiagonalOrder(mat))