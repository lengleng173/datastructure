class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        import heapq
        a=[]
        res=[]
        dic=dict()
        for i in words:
            dic[i]=dic.get(i,0)+1
        for key,value in dic.items():
            heapq.heappush(a,(-value,key))
        for _ in range(k):
            x=heapq.heappop(a)
            res.append(x[1])
        return res