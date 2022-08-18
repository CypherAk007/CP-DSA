# 198. House Robber-space optimized sol.

class Solution:
    def rob(self, nums: List[int]) -> int:
        temp1=[]
        temp2=[]
        n=len(nums)
        if n==1: #if array has single elemnt return it
            return nums[0]
        for i in range(n):
            if i!=0:
                #exclude the 0th house starthouse
                temp1.append(nums[i])
            if i!=n-1:
                #exclude the last house
                temp2.append(nums[i])
        return max(self.houseRobber(temp1),self.houseRobber(temp2))
        
    def houseRobber(self,nums):
        n=len(nums)
        prev=nums[0]
        prev2=0
        for i in range(1,n):
            pick=nums[i]
            if i>1:
                pick+=prev2
            notp=0+prev
            curi=max(pick,notp)
            prev2=prev
            prev=curi
        return prev