class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         Linear pass (one pass)-
#         cost=current profit
        # profit is maxprofit on any day till now
        # mini=minimum cost on any day till now
        # init
        mini=prices[0]
        profit=0
        n=len(prices)
        for i in range(1,n):
            cost=prices[i]-mini
            profit=max(profit,cost)
            mini=min(mini,prices[i])
        return profit
                