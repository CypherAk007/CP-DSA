class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r=len(obstacleGrid)
        c=len(obstacleGrid[0])
        dp=[[-1]*c for i in range(r)]
        return self.helper(r-1,c-1,obstacleGrid,dp)
    # Basic recursion
    def helper(self,r,c,obstacleGrid,dp):
        if obstacleGrid[r][c]==1:
            return 0
        if r==0 and c==0:
            return 1
        if dp[r][c]!=-1:
            return dp[r][c]
        up=left=0
        if r>0:
            up=self.helper(r-1,c,obstacleGrid,dp)
        if c>0:
            left=self.helper(r,c-1,obstacleGrid,dp)
        dp[r][c]=up+left
        return dp[r][c]
            