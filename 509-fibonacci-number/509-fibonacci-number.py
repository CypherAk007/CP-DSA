class Solution:
    # Tabulation(BottomUp)+Space Optimized - Tc=O(n)  Sc=O(1)
    def fib(self, n: int) -> int:
        return self.helper(n)
    def helper(self,n):
        prev2=0
        prev=1
        # base case
        if n==0:
            return prev2
        if n==1:
            return prev
        for i in range(2,n+1):
            curi=prev+prev2
            prev2=prev
            prev=curi
        return prev
        