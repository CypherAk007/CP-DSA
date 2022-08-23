class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[[0]*(amount+1) for i in range(n)]
        x=self.cchelperTab(n-1,amount,coins,dp)
        if x==float('inf'):
            return -1
        return x
    
# SIMPLE RECURSION + MEMOIZATION
    def cchelper(self,idx,t,coins,dp):
        # bc
        if idx==0:
          if t%coins[idx]==0:
            return t//coins[idx]
          else:
            return float('inf')
        
        if dp[idx][t]!=-1:
            return dp[idx][t]
        np=0+self.cchelper(idx-1,t,coins,dp)
        p=float('inf')
        if coins[idx]<=t:
          p=1+self.cchelper(idx,t-coins[idx],coins,dp)
        dp[idx][t]=min(p,np)
        return dp[idx][t]
    
    def cchelperTab(self,idx,t,coins,dp):
        # bc
        n=len(coins)
        for T in range(0,t+1):
            if T % coins[0]==0:
                dp[0][T]=T//coins[0]
            else:
                dp[0][T]=float('inf')
        
        for ind in range(1,n):
            
            for T in range(1,t+1):
                
                np=0+dp[ind-1][T]
                
                p=float('inf')
                if coins[ind]<=T:
                    p=1+dp[ind][T-coins[ind]]
                    
                dp[ind][T]=min(p,np)
        
        return dp[n-1][t]