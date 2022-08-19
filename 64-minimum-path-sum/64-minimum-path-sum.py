class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        dp=[[-1]*c for i in range(r)]
        return self.helper(r-1,c-1,grid,dp)
    
    # using recursion+memo
    def helper(self,r,c,grid,dp):
        if r==0 and c==0:
            return grid[r][c]
        if (r<0 or c<0):
            return float('inf') #we return max as we dont consider this relation
        if dp[r][c]!=-1:
            return dp[r][c]
        # up
        up=grid[r][c]+self.helper(r-1,c,grid,dp)
        # left
        left=grid[r][c]+self.helper(r,c-1,grid,dp)
        dp[r][c]= min(up,left)
        return dp[r][c]
            
            