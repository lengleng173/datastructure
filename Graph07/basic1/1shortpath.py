# 给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。

# 二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n - 1)）的路径，该路径同时满足下述要求：

# 路径途经的所有单元格的值都是 0 。
# 路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。
# 畅通路径的长度 是该路径途经的单元格总数。

 

# 示例 1：


# 输入：grid = [[0,1],[1,0]]
# 输出：2
# 示例 2：


# 输入：grid = [[0,0,0],[1,1,0],[1,1,0]]
# 输出：4
# 示例 3：

# 输入：grid = [[1,0,0],[1,1,0],[1,1,0]]
# 输出：-1
from typing import List
# class Solution:
#     def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
#         dis=0
#         n=len(grid)
#         res=1000000000
#         vis=[[False] *n for _ in range(n)]
#         ort=[[-1,-1],[-1,0],[0,-1],[1,0],[0,1],[1,1],[-1,1],[1,-1]]
#         def dfs(x,y,dis):
#             nonlocal res
#             if x==n-1 and y==n-1:
#                 res=min(dis,res)
#             elif vis[x][y]==False:
#                 vis[x][y]=True
#                 for o in ort:
#                     nx=x+o[0]
#                     ny=y+o[1]
#                     if nx>=0 and nx<n and ny>=0 and ny<n and grid[nx][ny]==0:
#                         dfs(nx,ny,dis+1)
#                 vis[x][y]=False
#         dfs(0,0,1)
#         return res
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ort=[[-1,-1],[-1,0],[0,-1],[0,1],[1,0],[1,1],[1,-1],[-1,1]]
        n=len(grid)
        vis = [[False for _ in range(n)] for _ in range(n)]
        q=deque()
        if grid[0][0]==1:
            return -1
        q.append([0,0,0])
        vis[0][0]=True
        while q:
            x,y,dis=q.popleft()
            if x==n-1 and y==n-1:
                return dis
            for o in ort:
                nx=o[0]+x
                ny=o[1]+y
                if nx>=0 and nx<n and ny>=0 and ny<n and grid[nx][ny]==0 and vis[nx][ny]==False:
                    vis[nx][ny]=True
                    q.append([nx,ny,dis+1])
            
        return -1
so=Solution()
G=[[0,0,0],[1,1,0],[1,1,0]]
print(so.shortestPathBinaryMatrix(G))