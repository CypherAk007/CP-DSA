class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        vis=[[0]*m for i in range(n)]
        dr=[-1,0,1,0]
        dc=[0,1,0,-1]
        cnt=0
        for row in range(0,n):
            for col in range(0,m):
                if (vis[row][col]==0 and grid[row][col]=='1'):
                    
                    cnt+=1
                    # self.bfs(row,col,vis,grid)
                    self.dfs(row,col,vis,grid,n,m,dr,dc)
                    
        return cnt
    
    def bfs(self,row,col,vis,grid):
        vis[row][col]=1
        q=[]
        q.append([row,col])
        n=len(grid)
        m=len(grid[0])
        while(len(q)!=0):
            node=q.pop(0)
            row=node[0]
            col=node[1]
            
            # now traverse in its neighbours
            for delrow in range(-1,2): #from [-1,0,1]
                for delcol in range(-1,2): #from [-1,0,1]
                    if delrow==0 or delcol==0:
                        nrow=row+delrow
                        ncol=col+delcol
                        if nrow>=0 and nrow<n and ncol>=0 and ncol<m and grid[nrow][ncol] == '1' and vis[nrow][ncol]==0:
                            vis[nrow][ncol]=1
                            q.append([nrow,ncol])
    
    def dfs(self,row,col,vis,grid,n,m,dr,dc):
        vis[row][col]=1
        for i in range(4):
            nr=row+dr[i]
            nc=col+dc[i]
            if nr>=0 and nr<n and nc>=0 and nc<m and grid[nr][nc]=='1' and vis[nr][nc]==0:
                self.dfs(nr,nc,vis,grid,n,m,dr,dc)
            
                        
                    
        