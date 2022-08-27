class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        dp=[[-1]*(m+1)for i in range(n+1)]
        return self.helper(n,m,word1,word2,dp)
    
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