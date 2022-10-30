class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        lo=max(nums)
        hi=sum(nums)
        res=max(nums)
        while(lo<=hi):
            mid=lo+(hi-lo)//2
            if self.isValid(nums,m,mid)==True:
                res=mid
                hi=mid-1
            else:
                lo=mid+1
        return res
    
    def isValid(self,nums,m,mid):
        s=1
        summ=0
        for i in range(len(nums)):
            summ+=nums[i]
            if summ>mid:
                s+=1
                summ=nums[i]
            if s>m:
                return False
        return True
    