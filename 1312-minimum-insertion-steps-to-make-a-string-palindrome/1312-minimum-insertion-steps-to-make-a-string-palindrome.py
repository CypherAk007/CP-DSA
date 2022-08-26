class Solution:
    def minInsertions(self, s: str) -> int:
        return len(s)-self.longestPalindromeSubseq(s)
        
    def longestPalindromeSubseq(self, s: str) -> int:
        s1=s
        s2=s[::-1]
        return self.longestCommonSubsequence(s1,s2)
        
    def longestCommonSubsequence(self, text1, text2):
        n=len(text1)
        m=len(text2)
        
        # dp=[[-1]*(m) for i in range(n)]
        dp=[[0]*(m+1) for i in range(n+1)]
        
        # return self.helper(n-1,m-1,text1,text2,dp) replace n-1 and m-1 with n,m(shifting indexes)
        return self.helper(text1,text2,dp)
    
    # i===i-1 and j===j-1
    # Tabulation
    def helper(self,text1,text2,dp):
        # bc
        n=len(text1)
        m=len(text2)
        for j in range(0,m+1):
            dp[0][j]=0
        for i in range(0,n+1):
            dp[i][0]=0
            
        for idx1 in range(1,n+1):
            for idx2 in range(1,m+1):
                if text1[idx1-1]==text2[idx2-1]:
                    dp[idx1][idx2]=1 + dp[idx1-1][idx2-1]
                else:
                    dp[idx1][idx2]=0+ max(dp[idx1-1][idx2],dp[idx1][idx2-1])
        
        return dp[idx1][idx2]