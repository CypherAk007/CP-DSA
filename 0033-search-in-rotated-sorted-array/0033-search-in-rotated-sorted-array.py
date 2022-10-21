class Solution:
    # find the min element index
    # then search fm 0 to min-1 idx and min idx to end
    # if we get ans >-1 fm any return else RETURN -1

    
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        minidx=self.rotatedbsMin(nums,0,n-1,n)
        left=self.bs(nums,0,minidx-1,target)
        right=self.bs(nums,minidx,n-1,target)
        
        if left<0 and right<0:
            return -1 
        elif left<0:
            return right
        else:
            return left
    
    def rotatedbsMin(self,a,lo,hi,n):
        while(lo<=hi):
            if a[lo]<=a[hi]:
                return lo
            
            mid=lo+(hi-lo)//2
            nxt=(mid+1)%n
            prev=(mid+n-1)%n
            if a[mid]<=a[nxt] and a[mid]<=a[prev]:
                return mid
            if a[lo]<=a[mid]:
                lo=mid+1 
            elif a[mid]<=a[hi]:
                hi=mid-1 
        return -1
    
    def bs(self,a,lo,hi,t):
        while(lo<=hi):
            mid=lo+(hi-lo)//2
            if a[mid]==t:
                return mid
            if t<a[mid]:
                hi=mid-1 
            elif t>a[mid]:
                lo=mid+1 
        return -1