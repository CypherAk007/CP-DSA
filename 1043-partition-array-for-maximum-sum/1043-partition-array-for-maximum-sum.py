class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n=len(arr)
        dp=[-1]*(n)
        return self.helper(0,arr,n,k,dp)
    
    def helper(self,idx,arr,n,k,dp):
        if idx==n:
            return 0
        if dp[idx]!=-1:
            return dp[idx]
        maxAns=float('-inf')
        maxi=float('-inf')
        length=0
        for j in range(idx,min(n,idx+k)):
            length+=1
            maxi=max(maxi,arr[j])
            summ=(length*maxi)+self.helper(j+1,arr,n,k,dp)
            maxAns=max(maxAns,summ)
        dp[idx]=maxAns
        return dp[idx]