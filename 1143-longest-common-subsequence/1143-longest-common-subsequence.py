class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        
        # dp=[[-1]*(m) for i in range(n)]
        dp=[[-1]*(m+1) for i in range(n+1)]
        
        # return self.helper(n-1,m-1,text1,text2,dp) replace n-1 and m-1 with n,m(shifting indexes)
        return self.helper(n,m,text1,text2,dp)
    
    # i===i-1 and j===j-1
    # Tabulation
    def helper(self,idx1,idx2,text1,text2,dp):
        if idx1==0 or idx2==0: # idx shifted so -1 is treated as 0
            return 0
        
        if dp[idx1][idx2]!=-1:
            return dp[idx1][idx2]
        
        if text1[idx1-1]==text2[idx2-1]:
            dp[idx1][idx2]=1 + self.helper(idx1-1,idx2-1,text1,text2,dp)
            return dp[idx1][idx2]
        
        dp[idx1][idx2]=0+ max(self.helper(idx1-1,idx2,text1,text2,dp),self.helper(idx1,idx2-1,text1,text2,dp))
        return dp[idx1][idx2]
    
    