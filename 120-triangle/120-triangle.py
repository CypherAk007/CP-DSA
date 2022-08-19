class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        dp=[[-1]*n for i in range(n)]
        return self.helper(0,0,triangle,n,dp)
    
    # Simple Recursion
    def helper(self,i,j,triangle,n,dp):
        if i==n-1:
            return triangle[i][j]
        if dp[i][j]!=-1:
            return dp[i][j]
        down=triangle[i][j]+self.helper(i+1,j,triangle,n,dp)
        diag=triangle[i][j]+self.helper(i+1,j+1,triangle,n,dp)
        dp[i][j]=min(down,diag)
        return dp[i][j]
    