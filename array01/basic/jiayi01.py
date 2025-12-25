digits=list(map(int,input().split()))

num=int(''.join(map(str,digits)))
num+=1
num_str=str(num)
num_new=list(map(int,num_str))
print(num_new)