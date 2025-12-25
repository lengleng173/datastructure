nums=list(map(int,input().split()))
st=''.join(map(str,nums)).split('0')
max_num=0
for i in st :
    max_num=max(len(i),max_num)
print(max_num)