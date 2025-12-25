def addTwoNumbers(l1, l2):
    jinwei=0
    c=[]
    for i in range(max(len(l1),len(l2))):
        if i<min(len(l1),len(l2)):
            c.append((l1[i]+l2[i]+jinwei)%10)
            jinwei=(l1[i]+l2[i]+jinwei)//10
        elif i>=len(l1):

            c.append((l2[i]+jinwei)%10)
            jinwei=(l2[i]+jinwei)//10
        else:
            
            c.append((l1[i]+jinwei)%10)
            jinwei=(l1[i]+jinwei)//10
        
    if jinwei==1:
        c.append(1)
    return c

