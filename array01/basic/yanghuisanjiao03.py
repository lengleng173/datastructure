numRows=int(input())
a=[]
for i in range(1,numRows+1):
    b=[]
    for j in range(1,i+1):
        if j==1 or j==i:
            b.append(1)
        else:
            b.append(a[i-2][j-2]+a[i-2][j-1])
    a.append(b)
print(a)