class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # lastGoodIndexPos=len(nums)-1
        # for i in range(len(nums)-1,-1,-1):
        #     if i+nums[i]>=lastGoodIndexPos:
        #         lastGoodIndexPos=i
        # return lastGoodIndexPos==0
        
        n=len(nums)
        reachable = 0
        for i in range(n):
            if reachable<i:
                return False
            reachable=max(reachable,i+nums[i])
        return True
            