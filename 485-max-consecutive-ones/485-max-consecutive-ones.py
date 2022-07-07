class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount=0
        tempCount=0
        for i in range(len(nums)):
            if nums[i]==1:
                tempCount+=1
                
            else:
                maxCount=max(maxCount,tempCount)
                tempCount=0
                
        maxCount=max(maxCount,tempCount)
        return maxCount