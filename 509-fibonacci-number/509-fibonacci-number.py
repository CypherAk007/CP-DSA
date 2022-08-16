class Solution:
    # memoization(topdown) - Tc=O(n) linearpattern Sc=O(n)+O(n)[rec stack+dp array]
    def fib(self, n: int) -> int:
        dp=[-1]*(n+1)
        # print(dp)
        return self.helper(n,dp)
    def helper(self,n,dp):
        if n<=1:
            return n
        if dp[n]!=-1:
            return dp[n]
        dp[n] = self.helper(n-1,dp)+self.helper(n-2,dp)
        return dp[n]