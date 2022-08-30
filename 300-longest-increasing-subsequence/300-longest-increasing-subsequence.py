class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        # dp=[[-1]*(n+1)for i in range(n)] # n+1 for 1based idx.
        # return self.helper(0,-1,nums,n,dp) #[idx,prev_idx,nums,n]
        
        # return self.helperTabs(nums,n)
        
        return self.helperTabM2(nums,n)

    def helper(self,idx,prev_idx,nums,n,dp):
        # bc
        if idx==n:
            return 0
        
        if dp[idx][prev_idx+1]!=-1:
            return dp[idx][prev_idx+1]
        
        notTake=0+self.helper(idx+1,prev_idx,nums,n,dp)
        
        Take=float('-inf')
        if prev_idx==-1 or nums[idx]>nums[prev_idx]:
            Take=1+self.helper(idx+1,idx,nums,n,dp)
            
        dp[idx][prev_idx+1]=max(Take,notTake)
        return dp[idx][prev_idx+1]
    
    # Tabulation
    def helperTab(self,nums,n):
        dp=[[0]*(n+1)for i in range(n+1)] # n+1 for 1based idx.
        for idx in range(n-1,-1,-1):
            for prev_idx in range(idx-1,-2,-1): # idx-1 -> -1
                # while converting - 2nd param is always in +1 state 
                notTake=0+dp[idx+1][prev_idx+1]
        
                Take=float('-inf')
                if prev_idx==-1 or nums[idx]>nums[prev_idx]:
                    Take=1+dp[idx+1][idx+1]

                dp[idx][prev_idx+1]=max(Take,notTake)
        return dp[0][-1+1]
    
    # Tabulation + SpaceOptimization tc-O(n^2) sc-O(n)*2
    def helperTabs(self,nums,n):
        ahead=[0]*(n+1)
        cur=[0]*(n+1)
        
        for idx in range(n-1,-1,-1):
            for prev_idx in range(idx-1,-2,-1): # idx-1 -> -1
                # while converting - 2nd param is always in +1 state 
                notTake=0+ahead[prev_idx+1]
        
                Take=float('-inf')
                if prev_idx==-1 or nums[idx]>nums[prev_idx]:
                    Take=1+ahead[idx+1]

                cur[prev_idx+1]=max(Take,notTake)
            ahead=cur
                
        return ahead[-1+1]
    
    def helperTabM2(self,nums,n): #tc->O(n^2) sc->O(n)
        dp=[1]*(n)
        maxi=1
        for i in range(0,n):
            for prev in range(0,i):
                if nums[prev]<nums[i]:
                    dp[i]=max(dp[i],1+dp[prev])
            maxi=max(maxi,dp[i])
        return maxi
    