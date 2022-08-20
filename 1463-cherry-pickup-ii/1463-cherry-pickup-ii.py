class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        # dp[r][c][c]
        dp1=[]
        for i in range(r):
            t=[]
            for j in range(c):
                t2=[]
                for k in range(c):
                    t2.append(-1)
                t.append(t2)
            dp1.append(t)
        # print(dp1)
        # dp=[[[-1 for i in range(r+1)] for i in range(c+1)] for i in range(c+1)]
        # print(dp)
        # print(dp1==dp)
        return self.helper(0,0,c-1,grid,r,c,dp1) #(i,j1,j2)
    
    # Using Simple recursion + Memo
    def helper(self,i,j1,j2,grid,r,c,dp):
        # out of bound
        if (j1<0 or j1>=c or j2<0 or j2>=c):
            return float('-inf')
        # bc
        if i==r-1:
            if j1==j2:# if both land at the same cell
                return grid[i][j1]
            else:
                return grid[i][j1]+grid[i][j2]
        if dp[i][j1][j2]!=-1:
            return dp[i][j1][j2]
        maxi=0
        for dj1 in range(-1,2):#Alice
            for dj2 in range(-1,2):#bob wrt alice
                if j1==j2:
                    maxi=max(maxi,grid[i][j1]+self.helper(i+1,j1+dj1,j2+dj2,grid,r,c,dp))
                else:
                    maxi=max(maxi,grid[i][j1]+grid[i][j2]+self.helper(i+1,j1+dj1,j2+dj2,grid,r,c,dp))
        dp[i][j1][j2]=maxi
        return dp[i][j1][j2]