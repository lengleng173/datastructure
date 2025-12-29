# 输入一个递增排序的数组array和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，返回任意一组即可，如果无法找出这样的数字，返回一个空数组即可。
# 输入：
# [1,2,4,7,11,15],15

# 返回值：
# [4,11]

class Solution:
    def FindNumbersWithSum(self , array: List[int], sum: int) -> List[int]:
        # write code here
        l,r=0,len(array)-1
        while l<r:
            if array[l]+array[r]==sum:
                return[array[l],array[r]]
            if array[l]+array[r]<sum:
                l+=1
            else:
                r-=1