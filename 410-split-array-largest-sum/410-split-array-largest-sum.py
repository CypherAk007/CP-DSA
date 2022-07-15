class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # get the range
        start=max(nums)
        end=sum(nums)
        # print(start,end)
        
        # binary Search
        while(start<end):
            # try for the potential ans
            mid=start+(end-start)//2
            # calc how many pieces we can divide this in with max sum
            summ=0
            pieces=1 #init one piece
            for num in nums:
                if summ+num>mid:
                    # you cant add this in this subarr, make new one
                    # when we add this num to new subarr then summ=0 and summ+=new num
                    summ=num
                    pieces+=1 #new arr piece is made
                else:
                    summ+=num
            
            if pieces>m: # target has become small inc the target to get smaller pieces ie right half of the arr
                start=mid+1
            else:
                end=mid
        
        return end # here start==end we got our ans