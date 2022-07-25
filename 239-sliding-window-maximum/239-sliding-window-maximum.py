class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        out=[]
        temp=[]
        i=0
        j=0
        while(j<len(nums)):
            # 1->
            while(len(temp)>0 and temp[len(temp)-1]<nums[j]):
                temp.pop()
            
            temp.append(nums[j])
            if j-i+1<k:
                j+=1
            elif j-i+1==k:
                out.append(temp[0])
                
                if nums[i]==temp[0]:
                    temp.pop(0)
                i+=1
                j+=1
        return out
                    
                    