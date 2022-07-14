class Solution:
    def peakIndexInMountainArray(self, a: List[int]) -> int:
        # Binary Search
        l=0
        h=len(a)-1
        while(l<h):
            mid=l+(h-l)//2
            if a[mid]>a[mid+1]:
                # you are in desc part of the arr and this may be a potential ans so end!=mid-1
                # so look for the left side 
                h=mid
            else:
                # you are at the asc part of the arr
                l=mid+1
        # if start and end are pointing to same ele that is the ans
        # at every pt at start and end they have the best possible ans at that time
        # if only one ele remains thats the max ele
        return l
            
            