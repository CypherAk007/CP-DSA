from copy import copy
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        temp=[]
        nums.sort()
        pre=False # this is to denote wether the previous ele was taken or not
        self.helper(temp,ans,nums,0,pre)
        return ans
    
    def helper(self,temp,ans,nums,idx,pre):
        if idx==len(nums):
            ans.append(copy(temp))
            return 
        
        # ignore element
        # always pre is false as we ignore the previous element
        self.helper(temp,ans,nums,idx+1,False)
        # if previous element == current element and we ignore the previous ele 
        # then ignore now also so return 
        if(idx>0 and nums[idx]==nums[idx-1]and not pre):
            return
        
        # take the element
        temp.append(nums[idx])
        # pre=True as we have taken the previous element
        self.helper(temp,ans,nums,idx+1,True)
        temp.pop()
        
        
        return ans
        
    