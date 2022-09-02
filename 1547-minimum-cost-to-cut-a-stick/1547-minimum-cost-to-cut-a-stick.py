class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        c=len(cuts)
        cuts.append(n)
        cuts.insert(0,0)
        cuts.sort()
        dp=[[-1]*(c+1) for i in range(c+1)]
        # return self.helper(1,c,cuts,n,dp)
        return self.helperTab(cuts,c,n)
    
    def helper(self,i,j,cuts,n,dp):
        if (i>j):
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        
        mini=float('inf')
        for idx in range(i,j+1):
            cost=cuts[j+1]-cuts[i-1]+self.helper(i,idx-1,cuts,n,dp)+self.helper(idx+1,j,cuts,n,dp)
            
            mini=min(mini,cost)
        dp[i][j]=mini
        return dp[i][j]
    
    def helperTab(self,cuts,c,n):
        dp=[[0]*(c+2)for i in range(c+2)]
        for i in range(c,0,-1):
            for j in range(1,c+1):
                # bc
                if i>j:
                    continue
                mini=float('inf')
                for idx in range(i,j+1):
                    cost=cuts[j+1]-cuts[i-1]+dp[i][idx-1]+dp[idx+1][j]
                    mini=min(mini,cost)
                dp[i][j]=mini
        return dp[1][c]