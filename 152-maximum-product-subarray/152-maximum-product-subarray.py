class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)#init if [-1]is arr then -1 is returned
        curmax=1
        curmin=1
        for i in range(len(nums)):
            # Edge Case
            if nums[i]==0:
                curmax=1
                curmin=1
                continue
        
            temp=curmax*nums[i]
            curmax=max(nums[i]*curmax,nums[i]*curmin,nums[i])
            curmin=min(temp,nums[i]*curmin,nums[i])
            res=max(res,curmax)
        return res