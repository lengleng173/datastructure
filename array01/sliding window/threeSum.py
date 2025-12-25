def threeSum( nums):
    """
        :type nums: List[int]
        :rtype: List[List[int]]
    """


    dic={}
    a=set()
    c=[]
    #字典
    for i in nums:
        dic[i]=dic.get(i,0)+1

    def panduan(x1,x2,x3):
        if (x1,x2,x3) in a or (x1,x3,x2) in a or (x2,x1,x3) in a or (x2,x3,x1) in a or (x3,x1,x2) in a or (x3,x2,x1) in a:
            return False
        else:
            return True
    #第一个数
    for left in range(len(nums)):
        dic[nums[left]]-=1
        right=len(nums)-1
        #第二个数
        while right>left:
                dic[nums[right]]-=1
                if dic.get(-(nums[left]+nums[right]),0)>0:
                    if panduan(nums[left],nums[right],-(nums[left]+nums[right])):
                        c.append([nums[left],nums[right],-(nums[left]+nums[right])])
                        a.add((nums[left],nums[right],-(nums[left]+nums[right])))
                    #加个判断

                dic[nums[right]]+=1
                right-=1
        dic[nums[left]]+=1

    return c




print(threeSum([-1,0,1,2,-1,-4]))