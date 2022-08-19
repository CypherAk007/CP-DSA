class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        r=len(matrix)
        c=len(matrix[0])
        dp=[[0]*c for i in range(r)]
        
        return self.helper(matrix,dp)
      
    
    # Using basic recursion + memoization
    def helper(self,matrix,dp):
        n=len(matrix)
        m=len(matrix[0])
        # bc
        for j in range(m):
            dp[0][j]=matrix[0][j]
        
        for i in range(1,n):
            for j in range(0,m):
                straight=matrix[i][j]+dp[i-1][j]
                
                leftdiag=matrix[i][j]
                if j-1>=0:
                    leftdiag+=dp[i-1][j-1]
                else:
                    leftdiag=float('inf')
                    
                rightdiag=matrix[i][j]
                if j+1<m:
                    rightdiag+=dp[i-1][j+1]
                else:
                    rightdiag=float('inf')
                    
                dp[i][j]=min(straight,min(leftdiag,rightdiag))
        
        mini=float('inf')
        for j in range(0,m):
            mini=min(mini,dp[n-1][j])
            
        return mini
    