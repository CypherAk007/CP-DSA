class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*n
        cnt=[1]*n
        maxi=1
        for i in range(0,n):
            for prev in range(0,i):
                if nums[prev]<nums[i] and 1+dp[prev]>dp[i]:
                    dp[i]=1+dp[prev]
                    
                    # inherit the count from prev's count
                    cnt[i]=cnt[prev]
                elif(nums[prev]<nums[i] and 1+dp[prev]==dp[i]):
                    # The length of the lis is reapeating so increase the count value
                    cnt[i]+=cnt[prev]
            maxi=max(maxi,dp[i])
        
        # return the cnt value at maxi-dp[maxi]-cnt[maxi]
        # but if the cnt value is repeating then sum them and return them
        nos=0
        for i in range(n):
            if dp[i]==maxi:
                nos+=cnt[i]
        return nos
                    