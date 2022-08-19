class Solution:
    
    def uniquePaths(self, r: int, c: int) -> int:
        dp=[[0]*c for i in range(r)]
        return self.helper(r,c,dp)
    # Tabulation
    def helper(self,r,c,dp):
        for i in range(0,r):
            for j in range(0,c):
                if i==0 and j==0:
                    dp[i][j]=1
                else:
                    up=0
                    left=0
                    if i>0:
                        up=dp[i-1][j]
                    if j>0:
                        left=dp[i][j-1]
                    dp[i][j]=up+left
        return dp[r-1][c-1]
        