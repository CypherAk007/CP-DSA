class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)
        # return self.helperRecursion(n-1,m-1,s,t)
        dp=[[-1]*m for i in range(n)]
        return self.helperMemoization(n-1,m-1,s,t,dp)
    
    def helperRecursion(self,i,j,s,t):
        # bc
        if j<0:
            return 1
        if i<0:
            return 0
        
        if s[i]==t[j]:
            return self.helperRecursion(i-1,j-1,s,t)+self.helperRecursion(i-1,j,s,t)
        
        return self.helperRecursion(i-1,j,s,t)
        
    def helperMemoization(self,i,j,s,t,dp):
        # bc
        if j<0:
            return 1
        if i<0:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        
        if s[i]==t[j]:
            dp[i][j]=self.helperMemoization(i-1,j-1,s,t,dp)+self.helperMemoization(i-1,j,s,t,dp)
            return dp[i][j]
        
        dp[i][j]=self.helperMemoization(i-1,j,s,t,dp)
        return dp[i][j]
        