class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        dp=[[-1]*(m)for i in range(n)]
        return self.helper(n-1,m-1,word1,word2,dp)
    
    # Recursion + memoization
    def helper(self,i,j,s1,s2,dp):
        # bc
        if i<0:
            return j+1
        if j<0:
            return i+1
        
        if dp[i][j]!=-1:
            return dp[i][j]
        
        if s1[i]==s2[j]:
            return 0+self.helper(i-1,j-1,s1,s2,dp)
        else:
            c1=1+self.helper(i,j-1,s1,s2,dp) #ins
            c2=1+self.helper(i-1,j,s1,s2,dp) #del
            c3=1+self.helper(i-1,j-1,s1,s2,dp) #replace
        dp[i][j]=min(c1,min(c2,c3))
        return dp[i][j]