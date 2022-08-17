class Solution:
    def rob(self, nums: List[int]) -> int:
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
        