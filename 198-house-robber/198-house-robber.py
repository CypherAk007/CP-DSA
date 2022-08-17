class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[-1]*(len(nums)-1+1)
        return self.maxsum(len(nums)-1,nums,dp)
    def maxsum(self,idx,a,dp):
        if idx==0:
            return a[idx]
        if idx<0:
            return 0
        if dp[idx]!=-1:
            return dp[idx]
        pick=a[idx]+self.maxsum(idx-2,a,dp)
        notp=0+self.maxsum(idx-1,a,dp)
        dp[idx]=max(pick,notp)
        return dp[idx]