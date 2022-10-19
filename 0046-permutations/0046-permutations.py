from copy import copy
class Solution:
    def permute(self, nums):
        # return self.helper(nums)
        
        ans=[]
        self.helper2(nums,0,ans)
        return ans
    
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
    
    def helper2(self,nums,i,ans):
        # bc
        if i==len(nums):
            ans.append(copy(nums))
            return 
        
        for j in range(i,len(nums)):
            nums[i],nums[j]=nums[j],nums[i]
            self.helper2(nums,i+1,ans)
            nums[i],nums[j]=nums[j],nums[i]
    
            
        
    