class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[-1]*(3)for i in range(n)]
        return self.helper(0,1,prices,n,dp)
    
    # RECURSION + Memo
    def helper(self,idx,buy,prices,n,dp):
        # bc
        if idx==n:
            return 0
        
        if dp[idx][buy]!=-1:
            return dp[idx][buy]
        
        if buy:
            dp[idx][buy]=max(-prices[idx]+self.helper(idx+1,0,prices,n,dp),
                        0+self.helper(idx+1,1,prices,n,dp))
            return dp[idx][buy]
        else:
            dp[idx][buy]=max(prices[idx]+self.helper(idx+1,1,prices,n,dp),
                      0+self.helper(idx+1,0,prices,n,dp))
            return dp[idx][buy]
        