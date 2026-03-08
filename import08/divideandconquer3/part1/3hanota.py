def hanota(n,A,B,C):
    if n==0:
        C.append(A.pop())
    else:
        hanota(n-1,A,[],B)
        hanota(0,A,[],C)
        hanota(n-1,B,[],C)

        
        
A=[5,4,3,2,1,0]
B=[]
C=[]
hanota(5,A,B,C)
print(C)