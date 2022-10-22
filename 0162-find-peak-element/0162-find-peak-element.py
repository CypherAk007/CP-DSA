class Solution:
    def findPeakElement(self, a: List[int]) -> int:
        # # Binary Search
        # l=0
        # h=len(a)-1
        # while(l<h):
        #     mid=l+(h-l)//2
        #     if a[mid]>a[mid+1]:
        #         # you are in desc part of the arr and this may be a potential ans so end!=mid-1
        #         # so look for the left side 
        #         h=mid
        #     else:
        #         # you are at the asc part of the arr
        #         l=mid+1
        # # if start and end are pointing to same ele that is the ans
        # # at every pt at start and end they have the best possible ans at that time
        # # if only one ele remains thats the max ele
        # return l
        
        # Adithaya verma sol
        return self.findpeakAV(a)
        
    def findpeakAV(self,arr):
        if len(arr)==1:
            return 0
        lo=0
        hi=len(arr)-1
        while(lo<=hi):
            mid=lo+(hi-lo)//2
            if mid>0 and mid<len(arr)-1:
                if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                    return mid
                elif (arr[mid-1]>arr[mid]):
                    hi=mid-1
                else:
                    lo=mid+1
            elif mid==0:
                if  arr[0]>arr[1]:
                    return 0
                else:
                    return 1
            elif mid==len(arr)-1:
                if arr[len(arr)-1]>arr[len(arr)-2]:
                    return len(arr)-1
                else:
                    return len(arr)-2