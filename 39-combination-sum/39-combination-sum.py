from copy import copy
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        temp=[]
        self.helper(target,temp,ans,0,candidates)
        return ans
    
    def helper(self,t,temp,ans,idx,candidates):
        # if we get the target
        if t==0:
            ans.append(copy(temp))
            return
        # if target becomes negitive 
        if t<0:
            return
        # if we reach the end of candidates and target is not meet
        if idx==len(candidates):
            return 
        
        # we ignore the ith ele
        self.helper(t,temp,ans,idx+1,candidates)
        
        # we pick the element then we dont increment ith ptr as 
        # we might need the element in future to add it
        temp.append(candidates[idx])
        self.helper(t-candidates[idx],temp,ans,idx,candidates)
        temp.pop() # removal of prev changes -  # back tracking
        
        return ans
        
            