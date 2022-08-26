class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)
        
        # return self.helperRecursion(n-1,m-1,s,t)
        
        # dp=[[-1]*m for i in range(n)]
        # return self.helperMemoization(n-1,m-1,s,t,dp)
        
        # dp=[[-1]*(m+1) for i in range(n+1)]
        # return self.helperMemoization1(n,m,s,t,dp)
    
        return self.helperTab(s,t)
    
    def helperRecursion(self,i,j,s,t):
        # bc
        if j<0:
            return 1
        if i<0:
            return 0
        
        if s[i]==t[j]:
            return self.helperRecursion(i-1,j-1,s,t)+self.helperRecursion(i-1,j,s,t)
        
        return self.helperRecursion(i-1,j,s,t)
        
    
    def helperMemoization1(self,i,j,s,t,dp): #converted to 1-based indexing
        # bc
        if j==0:
            return 1
        if i==0:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        
        if s[i-1]==t[j-1]:
            dp[i][j]=self.helperMemoization1(i-1,j-1,s,t,dp)+self.helperMemoization1(i-1,j,s,t,dp)
            return dp[i][j]
        
        dp[i][j]=self.helperMemoization1(i-1,j,s,t,dp)
        return dp[i][j]
    
    def helperTab(self,s,t):
        n=len(s)
        m=len(t)
        dp=[[0]*(m+1) for i in range(n+1)]
        # BC
        for i in range(0,n+1):
            dp[i][0]=1 
        # fm 1->m+1 cause ith loop runs fm dp[0][0]=1 and jth also dp[0][0]=0 overlap
        for j in range(1,m+1): 
            dp[0][j]=0
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][m]
    
        
        
    
        