class Solution:
    # right half-> 1st instance -> odd index, 2nd instance-> even index
    # left half-> 2st instance ->even index , 2nd instance->  odd index
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo=0
        hi=len(nums)-2
        res=-1
        while(lo<=hi):
            mid=lo+(hi-lo)//2
            val=nums[mid]
            if mid%2==0 and nums[mid+1]==val:
                lo=mid+1 
            elif mid%2==1 and nums[mid-1]==val:
                lo=mid+1 
            else:
                res=mid
                hi=mid-1
        # print(res,nums[res])
        return nums[res]