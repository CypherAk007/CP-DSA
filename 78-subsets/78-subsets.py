from copy import copy

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        temp=[]
        self.helper(temp,ans,nums,0)
        return ans
    def helper(self,temp,ans,nums,idx):
        if idx==len(nums):
            ans.append(copy(temp))
            return
            # return ans
        # take the ith ele
        temp.append(nums[idx])
        self.helper(temp,ans,nums,idx+1)
        # while returning fm call resotre the arr as normal without nums[i]
        temp.pop()
        
        #leve the element
        self.helper(temp,ans,nums,idx+1)
        return ans