from copy import copy
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        self.helper2(nums,0,ans)
        return ans
        
    def helper2(self,nums,i,ans):
        # bc
        if i==len(nums):
            ans.append(copy(nums))
            return 
        
        s=set()
        for j in range(i,len(nums)):
            
            if nums[j] in s:
                continue
            s.add(nums[j])
            nums[i],nums[j]=nums[j],nums[i]
            self.helper2(nums,i+1,ans)
            nums[i],nums[j]=nums[j],nums[i]
    
        
        
        