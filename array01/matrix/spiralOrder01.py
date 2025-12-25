def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    c=[]
    if len(matrix)==1 or len(matrix[0])==1:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                c.append(matrix[i][j])
        return c

    times = min(len(matrix),len(matrix[0]))//2+min(len(matrix),len(matrix[0]))%2
    for i in range(times):
        print('第{}圈'.format(i+1))
        #遍历四周
        for x1 in range(i,len(matrix[0])-i):
            print('x1:{}'.format(matrix[i][x1]))
            pre1=[i,x1]
            c.append(matrix[i][x1])
        for x2 in range(i+1,len(matrix)-i):
            print('x2:{}'.format(matrix[x2][len(matrix[0])-1-i]))
            pre2=[x2,len(matrix[0])-1-i]
            c.append(matrix[x2][len(matrix[0])-1-i])
        for x3 in range(len(matrix[0])-i-2,i,-1):

            print('x3:{}'.format(matrix[len(matrix)-i-1][x3]))
            if [len(matrix)-i-1,x3]==pre1 or [len(matrix)-i-1,x3]==[i,x1-1]:
                break
            c.append(matrix[len(matrix)-i-1][x3])
        for x4 in range(len(matrix)-i-1,i,-1):
            print('x4:{}'.format(matrix[x4][i]))
            if [x4,i]==pre1 or [x4,i]==[i,x1-1]:
                break
            c.append(matrix[x4][i])
    return c

matrix=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
print(spiralOrder(matrix))