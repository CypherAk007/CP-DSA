class Solution:
    def updateMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        m=len(grid[0])
        vis=[[0 for x in range(m)]for i in range(n)]
        dist=[[0 for x in range(m)] for i in range(n)]
        q=[]
        # init store all the 1's in queue and mark vis
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    q.append([[i,j],0]) #[[i,j],dist]
                    vis[i][j]=1 #Also mark visited as 1
                else:
                    vis[i][j]=0
        
        delrow=[-1,0,1,0]
        delcol=[0,1,0,-1]
        
        while(len(q)!=0):
            node=q.pop(0)
            row=node[0][0]
            col=node[0][1]
            steps=node[1]
            # update the dist matrix with steps
            dist[row][col]=steps
            
            for i in range(4): #[0,1,2,3] to access the delrow/col
                nrow=row+delrow[i]
                ncol=col+delcol[i]
                if nrow>=0 and nrow<n and ncol>=0 and ncol<m :
                    if  vis[nrow][ncol]==0:
                        vis[nrow][ncol]=1
                        q.append([[nrow,ncol],steps+1])
        return dist