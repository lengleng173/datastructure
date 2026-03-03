l=[35,63,48,9,86,24,53,11]

def bubblesort(l):
    for i in range(len(l)):
        flag=False
        for j in range(i,len(l)):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
                flag=True
        if flag==False:
            return
bubblesort(l)
print(l)