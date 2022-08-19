class Solution:
    # Basic recursion
    
    def uniquePaths(self, r: int, c: int) -> int:
        dp=[[-1]*c for i in range(r)]
        return self.helper(r-1,c-1,dp)
    def helper(self,r,c,dp):
        if r==0 and c==0:
            return 1
        if r<0 or c<0:
            return 0
        if dp[r][c]!=-1:
            return dp[r][c]
        left = self.helper(r-1,c,dp)
        right = self.helper(r,c-1,dp)
        dp[r][c]=left+right
        return dp[r][c]