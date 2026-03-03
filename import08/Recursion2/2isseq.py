def isseq(x):
    if len(x)<=1:
        return True
    return x[0]<x[1] and isseq(x[1:])

print(isseq([1,2,3,4,5,6]))
print(isseq([4,3,8,1,9]))