class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        dp=[[-1]*(m+1)for i in range(n+1)]
        # return self.helper(n,m,word1,word2,dp)
        return self.helperTab(word1,word2)
    
    # Recursion + memoization  (0-BASED ===> 1-BASED)
    def helper(self,i,j,s1,s2,dp):
        # bc
        if i==0:
            return j
        if j==0:
            return i
        
        if dp[i][j]!=-1:
            return dp[i][j]
        
        if s1[i-1]==s2[j-1]:
            dp[i][j]=0+self.helper(i-1,j-1,s1,s2,dp)
            return dp[i][j] 
        else:
            c1=1+self.helper(i,j-1,s1,s2,dp) #ins
            c2=1+self.helper(i-1,j,s1,s2,dp) #del
            c3=1+self.helper(i-1,j-1,s1,s2,dp) #replace
        dp[i][j]=min(c1,min(c2,c3))
        return dp[i][j]
    
    # Tabulation
    def helperTab(self,s1,s2):
        n=len(s1)
        m=len(s2)
        dp=[[0]*(m+1)for i in range(n+1)]
        
        # bc
        for i in range(n+1):
            dp[i][0]=i
        for j in range(m+1):
            dp[0][j]=j
            
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=0+dp[i-1][j-1]
                else:
                    dp[i][j]= 1+min(dp[i][j-1],min(dp[i-1][j],dp[i-1][j-1]))
                
        return dp[n][m]
    
    