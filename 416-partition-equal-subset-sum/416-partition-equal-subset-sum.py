class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totSum=sum(nums)
        if totSum%2==1:
            return False
        target=totSum/2
        
        n=len(nums)
        # dp[idx][target]
        dp=[[-1]*(int(target+1)) for i in range(n)]
        return self.helper(nums,n-1,int(target),dp)
    
    # Memoization
    def helper(self,nums,idx,target,dp):
        if target==0:
            return True
        if idx==0:
            return (nums[idx]==target)
        if dp[idx][target]!=-1:
            return dp[idx][target]
        np=self.helper(nums,idx-1,target,dp)
        p=False
        if target>=nums[idx]:
            p=self.helper(nums,idx-1,target-nums[idx],dp)
        dp[idx][target]=p or np
        return dp[idx][target]
    