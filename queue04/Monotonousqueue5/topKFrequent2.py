# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

 

# 示例 1：

# 输入：nums = [1,1,1,2,2,3], k = 2

# 输出：[1,2]
from typing import List
from queue import PriorityQueue

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=dict()
        for i in nums:
            dic[i]=dic.get(i,0)+1
        pq = PriorityQueue()
        for key,value in dic:
            pq.put((-1*value,key))
        a=[]
        while k!=0:
           a.append(pq.pop()[1]) 
           k-=1
        return a