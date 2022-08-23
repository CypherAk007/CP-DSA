class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[[-1]*(amount+1) for i in range(n)]
        x=self.cchelper(n-1,amount,coins,dp)
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