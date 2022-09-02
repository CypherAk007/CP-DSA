class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n=len(nums)
        nums.append(1)
        nums.insert(0,1)
        dp=[[-1]*(n+1)for i in range(n+1)]
        # return self.helper(1,n,nums,dp)
        return self.helperTab(nums,n)
    
    def helper(self,i,j,a,dp):
        if i>j:
            return 0
        maxi=float('-inf')
        if dp[i][j]!=-1:
            return dp[i][j]
        for idx in range(i,j+1):
            cost=a[i-1]*a[idx]*a[j+1]+self.helper(i,idx-1,a,dp)+self.helper(idx+1,j,a,dp)
            maxi=max(maxi,cost)
        dp[i][j]=maxi
        return dp[i][j]
    
    def helperTab(self,a,n):
        
        dp=[[0]*(n+2)for i in range(n+2)]
        for i in range(n,0,-1):
            for j in range(1,n+1):
                if i>j:
                    continue
                maxi=float('-inf')
                for idx in range(i,j+1):
                    cost=a[i-1]*a[idx]*a[j+1]+dp[i][idx-1]+dp[idx+1][j]
                    maxi=max(maxi,cost)
                dp[i][j]=maxi
        return dp[1][n]
                    