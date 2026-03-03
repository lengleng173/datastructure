def getLeastnums(arr,k):
    arr=sorted(arr)
    return arr[:k]
print(getLeastnums([3,2,1],2))