class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        
        return self.helper(prices,n)
    
    # Tabulation + spaceoptimized
    def helper(self,prices,n):
        ahead=[0]*2
        cur=[0]*2
        
        # bc
        ahead[0]=ahead[1]=0
        
        for idx in range(n-1,-1,-1):
            for buy in range(0,2):
                profit=0
                if buy:
                    profit=max(-prices[idx]+ahead[0],
                                0+ahead[1])
                else:
                    profit=max(prices[idx]+ahead[1],
                              0+ahead[0])
                cur[buy]=profit
            ahead=cur
            
        return ahead[1]
                    
        