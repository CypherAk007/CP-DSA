class Solution:
    def climbStairs(self, n: int) -> int:
        return self.helper(n)
    
    # SPACE OPTIMIZED SOL
    def helper(self,n):
        prev2=1
        prev=1
        # bc
        if n==0 :
            return prev2
        if n==1:
            return prev
        
        for i in range(2,n+1):
            cur=prev+prev2
            prev2=prev
            prev=cur
        return prev
        