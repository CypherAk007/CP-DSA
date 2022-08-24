class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        # dp=[[-1]*(amount+1) for i in range(n)]
        # return self.helper(n-1,amount,coins,dp)
        dp=[[0]*(amount+1) for i in range(n)]
        return self.tabhelper(amount,coins,dp,n)
    
    #SIMPLE RECURSION + MEMOIZATION
    def helper(self,idx,t,coins,dp):
        if idx==0:
            if t%coins[0]==0:
                return 1
            else:
                return 0
        if dp[idx][t]!=-1:
            return dp[idx][t]
        np=self.helper(idx-1,t,coins,dp)
        p=0
        if coins[idx]<=t:
            p=self.helper(idx,t-coins[idx],coins,dp)
        dp[idx][t]=np+p
        return dp[idx][t]
    
    #Tabulation
    def tabhelper(self,target,coins,dp,n):
        for T in range(0,target+1):
            if T%coins[0]==0:
                dp[0][T]=1
            else:
                dp[0][T]=0
        
        for idx in range(1,n):
            for t in range(0,target+1):
                np=dp[idx-1][t]
                p=0
                if coins[idx]<=t:
                    p=dp[idx][t-coins[idx]]
                dp[idx][t]=np+p
                
        return dp[n-1][target]