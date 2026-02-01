from collections import deque
from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def perimeter(x,y):
            per=0
            if x==0 or grid[x-1][y]==0:
                per+=1
            if x==len(grid)-1 or grid[x+1][y]==0:
                per+=1
            if y==0 or grid[x][y-1]==0:
                per+=1
            if y==len(grid[0])-1 or grid[x][y+1]==0:
                per+=1
            return per

        q=deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    break
            if grid[i][j]==1:
                    break    
        q.append([i,j])
        ort=[[0,-1],[-1,0],[1,0],[0,1]]
        vis=[[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        vis[i][j]=True
        per=perimeter(i,j)
        while q:
            [x,y]=q.popleft()
            for o in ort:
                nx=x+o[0]
                ny=y+o[1]
                if nx>=0 and ny>=0 and nx<len(grid) and ny<len(grid[0]) and vis[nx][ny]==False and grid[nx][ny]==1:
                    vis[nx][ny]=True
                    per+=perimeter(nx,ny)
                    q.append([nx,ny])
        return per

so=Solution()
grid=[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
res=so.islandPerimeter(grid)
print(res)