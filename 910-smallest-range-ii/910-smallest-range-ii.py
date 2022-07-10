class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        ans=nums[n-1]-nums[0]
        smallest=nums[0]+k
        largest=nums[n-1]-k
        mi=0
        mx=0
        for i in range(n-1):
            mi=min(smallest,nums[i+1]-k)
            mx=max(largest,nums[i]+k)
            ans=min(ans,mx-mi)
        return ans