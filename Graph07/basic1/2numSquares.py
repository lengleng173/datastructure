class Solution:
    def numSquares(self, n: int) -> int:
        a=[]
        for i in range(1,101):
            a.append(i**2)
        print(a)

so=Solution()
so.numSquares(2)