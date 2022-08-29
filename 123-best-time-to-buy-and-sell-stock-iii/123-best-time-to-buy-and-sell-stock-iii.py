class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[[-1]*(3) for i in range(2)]for j in range(n)]
        # print(dp)
        return self.helper(prices,n,) # [idx,buy,cap,prices]
    
    # Tabulation
    def helper(self,prices,n,):
        dp=[[[0]*(3) for i in range(2)]for j in range(n+1)]
        #   NO NEED TO WRITE bc AS ALL THE VAL INIT ARE 0
        # if cap==0:
        #     return 0
        # if idx==n:
        #     return 0
        
        for idx in range(n-1,-1,-1):
            for buy in range(0,2):
                for cap in range(1,3): #cap starts fm 1 as in bc- cap==0: return 0
                    if buy==1:
                        dp[idx][buy][cap]=max(-prices[idx]+dp[idx+1][0][cap],
                                  0+dp[idx+1][1][cap])
                        
                    else:
                        dp[idx][buy][cap]=max(prices[idx]+dp[idx+1][1][cap-1],
                                  0+dp[idx+1][0][cap])
        return dp[0][1][2]