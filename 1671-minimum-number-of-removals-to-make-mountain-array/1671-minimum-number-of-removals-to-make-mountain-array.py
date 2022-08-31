class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n=len(nums)
        biotonicLen=self.longestBiotonicSequence(nums,n)
        # print(biotonicLen)
        return n-biotonicLen
    def longestBiotonicSequence(self,nums,n):
        # LIS tc-O(n^2)
        dp1=[1]*n
        for i in range(n):
            for prev in range(i):
                if nums[prev]<nums[i] and 1+dp1[prev]>dp1[i]:
                    dp1[i]=1+dp1[prev]
        
        # LDStc-O(n^2)
        dp2=[1]*n
        for i in range(n-1,-1,-1):
            for prev in range(n-1,i,-1):
                if nums[prev]<nums[i] and 1+dp2[prev]>dp2[i]:
                    dp2[i]=1+dp2[prev]
        
        maxi=0
        for i in range(n):
            if dp1[i]>1 and dp2[i]>1:
                maxi=max(maxi,dp1[i]+dp2[i]-1)
        return maxi