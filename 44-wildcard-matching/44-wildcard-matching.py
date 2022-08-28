class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n=len(p)
        m=len(s)
        # return self.helperRec(n-1,m-1,p,s)
        dp=[[-1]*(m)for i in range(n)]
        return self.helper(n-1,m-1,p,s,dp)
    
    def helperRec(self,i,j,p,s):
        # bc
        if i<0 and j<0 :return True
        if i<0 and j>=0:return False
        if i>=0 and j<0:
            for k in range(0,i+1):
                if p[k]!='*':
                    return False
            return True
    
        if p[i]==s[j] or p[i]=='?':
            return self.helperRec(i-1,j-1,p,s)
            
        if p[i]=='*':
            return self.helperRec(i-1,j,p,s)  or self.helperRec(i,j-1,p,s)
            
        return False
    
    # REC+MEMOIZATION
    def helper(self,i,j,p,s,dp):
        # bc
        if i<0 and j<0 :return True
        if i<0 and j>=0:return False
        if i>=0 and j<0:
            for k in range(0,i+1):
                if p[k]!='*':
                    return False
            return True
        
        if dp[i][j]!=-1:
            return dp[i][j]
        
        if p[i]==s[j] or p[i]=='?':
            dp[i][j]=self.helper(i-1,j-1,p,s,dp)
            return dp[i][j]
        
        if p[i]=='*':
            dp[i][j]=self.helper(i-1,j,p,s,dp)or self.helper(i,j-1,p,s,dp)
            return dp[i][j]
        
        dp[i][j]=False #if there is no match
        return dp[i][j]