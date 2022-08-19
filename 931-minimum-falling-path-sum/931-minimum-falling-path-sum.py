class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        r=len(matrix)
        c=len(matrix[0])
        mini=float('inf')
        # as we have varible starting point we check 
        # for all the values in the last row and take the min
        dp=[[-1]*c for i in range(r)]
        for j in range(c):
            ans= self.helper(r-1,j,matrix,dp)
            mini=min(mini,ans)
        return mini
    
    # Using basic recursion + memoization
    def helper(self,i,j,matrix,dp):
        if j<0 or j>=len(matrix[0]): # avoid the diagonal overflow
            return float('inf')
        
        if i==0:
            return matrix[0][j]#what ever is there on the jth col return
        
        if dp[i][j]!=-1:
            return dp[i][j]
        
        straight=matrix[i][j]+self.helper(i-1,j,matrix,dp)
        leftdiag=matrix[i][j]+self.helper(i-1,j-1,matrix,dp)
        rightdiag=matrix[i][j]+self.helper(i-1,j+1,matrix,dp)
        dp[i][j]=min(straight,min(leftdiag,rightdiag))
        return dp[i][j]