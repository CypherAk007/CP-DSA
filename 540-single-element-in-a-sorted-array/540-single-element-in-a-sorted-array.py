class Solution:
    # right half-> 1st instance -> odd index, 2nd instance-> even index
    # left half-> 2st instance ->even index , 2nd instance->  odd index
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-2
        while(low<=high):
            mid=(low+high)//2
            if mid%2==1: #Check for the 1st instance
                if nums[mid-1]==nums[mid]:
                    low =mid+1
                else:
                    high=mid-1
            else:
                if nums[mid+1]==nums[mid]:
                    low =mid+1
                else:
                    # we are at right half
                    high=mid-1
        return nums[low]