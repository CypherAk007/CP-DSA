class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d={}
        longestStreak = 0
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        currStreak = 1
        for i in range(len(nums)):
            if not nums[i]-1 in d:
                currNum = nums[i]
                currStreak =1
                currNum+=1
                while currNum in d:
                    currStreak+=1
                    currNum+=1
            longestStreak = max(longestStreak,currStreak)
        return longestStreak