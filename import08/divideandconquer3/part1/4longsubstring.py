def longsubstring(s,size):
    global cnt
    if s=="":
        return
    dic=dict()
    flag=False
    for i in s:
        dic[i]=dic.get(i,0)+1
    for key,value in dic.items():
        if value<size:
            flag=True
            l=s.split(key)
            for ll in l:
                longsubstring(ll,size)
    if flag==False:
        cnt=max(len(s),cnt)
    return cnt
cnt=0
print(longsubstring("ababbcaba",2))

