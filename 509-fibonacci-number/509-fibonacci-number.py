class Solution:
    def fib(self, n: int) -> int:
        dp=[-1]*(n+1)
        # print(dp)
        return self.helper(n,dp)
    def helper(self,n,dp):
        if n<=1:
            return n
        if dp[n]!=-1:
            return dp[n]
        out = self.helper(n-1,dp)+self.helper(n-2,dp)
        dp[n]=out
        return out