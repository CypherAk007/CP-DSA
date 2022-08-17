class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[-1]*(len(nums)-1+1)
        return self.maxsum(len(nums)-1,nums,dp)
    def maxsum(self,n,a,dp):
        dp[0]=a[0]
        for idx in range(1,n+1):
            pick=a[idx]
            if idx>1:
                pick+=dp[idx-2]
            notp=0+dp[idx-1]
            dp[idx]=max(pick,notp)
        return dp[n]
        