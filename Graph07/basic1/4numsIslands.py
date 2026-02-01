from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        q=deque()
        vis=[[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        def dfs(x,y):
            ort=[[-1,0],[0,-1],[1,0],[0,1]]
            for o in ort:
                nx=x+o[0]
                ny=y+o[1]
                if nx>=0 and nx<len(grid) and ny>=0 and ny<len(grid[0]) and vis[nx][ny]==False and grid[nx][ny]=='1':
                    vis[nx][ny]=True
                    dfs(nx,ny)
        cnt=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1' and vis[i][j]==False:
                    cnt+=1
                    dfs(i,j)
        return cnt
        
        
so=Solution()
grid = [
  ['1','1','1','1','0'],
  ['1','1','0','1','0'],
  ['1','1','0','0','0'],
  ['0','0','0','0','0']
]
print(so.numIslands(grid))