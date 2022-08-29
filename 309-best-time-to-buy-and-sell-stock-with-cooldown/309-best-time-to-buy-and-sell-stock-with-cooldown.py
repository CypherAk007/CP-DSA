class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[0]*(2)for i in range(n+2)]
        return self.helper(prices,n,dp)
    
    # Tabulation
    def helper(self,prices,n,dp):
        # bc
        dp[n][0]=dp[n][1]=0
        for idx in range(n-1,-1,-1):
            for buy in range(0,2):
                profit=0
                if buy:
                    profit=max(-prices[idx]+dp[idx+1][0],
                                0+dp[idx+1][1])
                else:
                    profit=max(prices[idx]+dp[idx+2][1],
                              0+dp[idx+1][0])
                dp[idx][buy]=profit
        return dp[0][1]