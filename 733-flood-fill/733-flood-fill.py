class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        iniColor= image[sr][sc] #init starting color
        ans=image
        delRow=[-1,0,+1,0]
        delCol=[0,+1,0,-1]
        self.dfs(sr,sc,image,color,delRow,delCol,iniColor,ans)
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
                
        