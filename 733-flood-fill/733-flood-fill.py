class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        iniColor= image[sr][sc] #init starting color
        ans=image
        delRow=[-1,0,+1,0]
        delCol=[0,+1,0,-1]
        n=len(image)
        m=len(image[0])
        # self.dfs(sr,sc,image,color,delRow,delCol,iniColor,ans)
        self.bfs(sr,sc,ans,image,delRow,delCol,n,m,color,iniColor)
        return ans
    
    def dfs(self,row,col,image,color,delRow,delCol,iniColor,ans):
        ans[row][col]=color
        n=len(image)
        m=len(image[0])
        for i in range(0,4):
            nrow=row+delRow[i]
            ncol=col+delCol[i]
            if nrow>=0 and nrow<n and ncol>=0 and ncol<m and image[nrow][ncol] == iniColor and ans[nrow][ncol] !=color:
                self.dfs(nrow,ncol,image,color,delRow,delCol,iniColor,ans)
                
    def bfs(self,row,col,ans,image,dr,dc,n,m,color,initcolor):
        q=[]
        q.append([row,col])
        ans[row][col]=color
        while(q):
            node=q.pop(0)
            r=node[0]
            c=node[1]
            for i in range(4):
                nr=r+dr[i]
                nc=c+dc[i]
                if nr>=0 and nr<n and nc>=0 and nc<m and image[nr][nc]==initcolor and ans[nr][nc]!=color:
                    q.append([nr,nc])
                    ans[nr][nc]=color
                    
            
        