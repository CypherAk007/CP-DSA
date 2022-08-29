class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[[-1]*(3) for i in range(2)]for j in range(n)]
        # print(dp)
        return self.helper(prices,n) # [idx,buy,cap,prices]
    
    # Tabulation+ space
    def helper(self,prices,n):
        after=[[0]*(3)for i in range(2)]
        cur=[[0]*(3)for i in range(2)]
        
        for idx in range(n-1,-1,-1):
            for buy in range(0,2):
                for cap in range(1,3): #cap starts fm 1 as in bc- cap==0: return 0
                    if buy==1:
                        cur[buy][cap]=max(-prices[idx]+after[0][cap],
                                  0+after[1][cap])
                        
                    else:
                        cur[buy][cap]=max(prices[idx]+after[1][cap-1],
                                  0+after[0][cap])
            after=cur
        return after[1][2]