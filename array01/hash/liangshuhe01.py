nums=list(map(int,input().split()))
target=int(input())
a=[]
# for i,n1 in enumerate(nums):
#     for  j,n2 in enumerate(nums):
#         if i==j:
#             continue
#         if n1+n2==target:
#             a.append(i)
#             a.append(j)
#             print(a)
for i,num in enumerate(nums):
    try:
        j=nums.index(target-num)
        if j==i:
            try:
                j=nums.index(target-num+1)
            except:
                continue
    except:
        continue
    a.append(i)
    a.append(j)
    print(a)

    '''
    字典优化
            # 初始化字典，用于存储 {已遍历数字: 其索引}
        num_map = {}
        # 遍历数组，同时获取索引和数字
        for index, num in enumerate(nums):
            # 计算当前数字需要的目标差值
            complement = target - num
            # 若差值在字典中，直接返回差值的索引和当前索引
            if complement in num_map:
                return [num_map[complement], index]
            # 若不在字典中，将当前数字和索引存入字典
            num_map[num] = index
        # 题目保证有解，此句仅为语法完整性
        return []
    '''
