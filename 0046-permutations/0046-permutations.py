from copy import copy
class Solution:
    def permute(self, nums):
        return self.helper(nums)
    
    def helper(self,nums):
        # bc
        if len(nums)==0:
            return [[]]
        
        ans=[]
        for i in range(0,len(nums)):
            nums2=[]
            for j in range(0,len(nums)):
                if i!=j:
                    nums2.append(nums[j])
            v=self.helper(nums2)
            for a in v:
                a.append(nums[i])
                ans.append(a)
                
        return ans
    