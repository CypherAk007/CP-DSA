class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r=len(obstacleGrid)
        c=len(obstacleGrid[0])
        dp=[[0]*c for i in range(r)]
        return self.helper(r-1,c-1,obstacleGrid,dp)
    # Tabulation
    def helper(self,r,c,obstacleGrid,dp):
        for i in range(0,r+1):
            for j in range(0,c+1):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                else:
                    if i==0 and j==0:
                        dp[i][j]=1
                    else:
                        up=left=0
                        if i>0:
                            up=dp[i-1][j]
                        if j>0:
                            left=dp[i][j-1]
                        dp[i][j]=up+left
        return dp[r][c]
            