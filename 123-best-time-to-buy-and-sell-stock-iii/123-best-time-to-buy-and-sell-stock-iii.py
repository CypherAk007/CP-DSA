class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[[-1]*(3) for i in range(2)]for j in range(n)]
        # print(dp)
        return self.helper(0,1,2,prices,n,dp) # [idx,buy,cap,prices]
    
    # RECURSION
    def helper(self,idx,buy,cap,prices,n,dp):
        # bc
        if cap==0:
            return 0
        if idx==n:
            return 0
        
        if dp[idx][buy][cap]!=-1:
            return dp[idx][buy][cap]
        
        if buy:
            dp[idx][buy][cap]=max(-prices[idx]+self.helper(idx+1,0,cap,prices,n,dp),
                      0+self.helper(idx+1,1,cap,prices,n,dp))
            return dp[idx][buy][cap]
        else:
            dp[idx][buy][cap]=max(prices[idx]+self.helper(idx+1,1,cap-1,prices,n,dp),
                      0+self.helper(idx+1,0,cap,prices,n,dp))
            return dp[idx][buy][cap]