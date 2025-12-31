class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack=[]
        day=[0]*len(temperatures)
        for idx,i in enumerate(temperatures):
            while len(stack)>0 and stack[-1][0]<i:
               ii,iidx=stack.pop()
               day[iidx]=idx-iidx
            stack.append([i,idx])  

        return day
    
so=Solution()
temperatures = [73,74,75,71,69,72,76,73]
print(so.dailyTemperatures(temperatures))