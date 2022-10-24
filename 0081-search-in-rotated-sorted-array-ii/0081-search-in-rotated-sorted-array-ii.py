class Solution:
    def search(self, nums, target):
        left=0
        right=len(nums)-1
        while(left<=right):
            if nums[left]==target or nums[right]==target:
                return True
            elif target>nums[left]:
                while(left<right and nums[left]==nums[left+1]):
                    left+=1
                left+=1
            elif target<nums[right]:
                while(left<right and nums[right]==nums[right-1]):
                    right-=1
                right-=1
            else:
                break
        return False