from copy import copy
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        temp=[]
        candidates.sort()
        pre=False
        self.helper(candidates,ans,temp,target,0,pre)
        return ans
    def helper(self,candidates,ans,temp,target,idx,pre):
        if target==0:
            ans.append(copy(temp))
            return 
        if target<0:
            return
        if idx==len(candidates):
            return
        
        self.helper(candidates,ans,temp,target,idx+1,False)
        if (idx>0 and candidates[idx]==candidates[idx-1] and not pre):
            return 
        
        temp.append(candidates[idx])
        self.helper(candidates,ans,temp,target-candidates[idx],idx+1,True)
        temp.pop()
        
        return ans