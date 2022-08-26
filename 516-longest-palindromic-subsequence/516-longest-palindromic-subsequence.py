class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s1=s
        s2=s[::-1]
        return self.longestCommonSubsequence(s1,s2)
        
    def longestCommonSubsequence(self, text1, text2):
        n=len(text1)
        m=len(text2)
        dp=[[-1]*(m) for i in range(n)]
        return self.helper(n-1,m-1,text1,text2,dp)
    
    # Simple recursion
    def helper(self,idx1,idx2,text1,text2,dp):
        if idx1<0 or idx2<0:
            return 0
        
        if dp[idx1][idx2]!=-1:
            return dp[idx1][idx2]
        
        if text1[idx1]==text2[idx2]:
            dp[idx1][idx2]=1 + self.helper(idx1-1,idx2-1,text1,text2,dp)
            return dp[idx1][idx2]
        
        dp[idx1][idx2]=0+ max(self.helper(idx1-1,idx2,text1,text2,dp),self.helper(idx1,idx2-1,text1,text2,dp))
        return dp[idx1][idx2]
    