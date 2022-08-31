class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n=len(nums)
        return self.helperTabM2PrintLIS(nums,n)
    def helperTabM2PrintLIS(self,nums,n): #tc->O(n^2) sc->O(n)
        dp=[1]*(n)
        d=[1]*(n)#hash array
        maxi=1
        lastIndex=0
        for i in range(0,n):
            d[i]=i #init store the idx of the hash array
            for prev in range(0,i):
                if nums[i]%nums[prev]==0 and 1+dp[prev]>dp[i]: #whenever the dp array is getting updated
                    dp[i]=1+dp[prev]
                    d[i]=prev#stores the previous guy
                    
            if dp[i]>maxi:
                maxi=dp[i]
                lastIndex=i
        temp=[]
        temp.append(nums[lastIndex])
        while (d[lastIndex]!=lastIndex):
            lastIndex=d[lastIndex]
            temp.append(nums[lastIndex])
        temp.reverse()
        # print(temp)
        return temp
    