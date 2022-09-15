class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # code here
        delrow=[-1,0,1,0]
        delcol=[0,1,0,-1]
        
        n=len(grid)
        m=len(grid[0])
        vis=[[0 for i in range(m)]for j in range(n)]
        
        # traverse the first row and last row
        for j in range(m):
            if grid[0][j]==1 and vis[0][j]==0:
                self.dfs(0,j,grid,vis,delrow,delcol)
            
            if grid[n-1][j]==1 and vis[n-1][j]==0:
                self.dfs(n-1,j,grid,vis,delrow,delcol)
        
        # traverse the first col and last col
        for i in range(n):
            if grid[i][0]==1 and vis[i][0]==0:
                self.dfs(i,0,grid,vis,delrow,delcol)
            
            if grid[i][m-1]==1 and vis[i][m-1]==0:
                self.dfs(i,m-1,grid,vis,delrow,delcol)
        
        c=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and vis[i][j]==0:
                    c+=1
        return c
        
    def dfs(self,row,col,grid,vis,delrow,delcol):
        vis[row][col]=1
        n=len(grid)
        m=len(grid[0])
        for i in range(4):
            nrow=row+delrow[i]
            ncol=col+delcol[i]
            if nrow>=0 and nrow<n and ncol>=0 and ncol<m and grid[nrow][ncol]==1 and vis[nrow][ncol]==0:
                self.dfs(nrow,ncol,grid,vis,delrow,delcol)