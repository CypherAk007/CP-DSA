# Keeping all the  positives to one side and negitives to one side
# making it a proble of two subsets where s1 - s2 = target

class Solution:
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        dp=[[-1]*(20*sum(nums)+1) for i in range(n)]
        return self.helper(n-1,target,nums,dp,target)
    
    def helper(self,idx,t,arr,dp,tar):
        # bc
        # if t==0:
        #     return 1
        if idx==-1:
            if t==0:
            # if arr[idx]==t:
                return 1
            
            else:
                return 0
        if dp[idx][t]!=-1:
            return dp[idx][t]
        a=self.helper(idx-1,t+arr[idx],arr,dp,tar)
        s=0
        # if arr[idx]<=t:
        s=self.helper(idx-1,t-arr[idx],arr,dp,tar)
        dp[idx][t]=a+s
        return dp[idx][t]
        # return a+s
        