class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]<=nums[len(nums)-1]:
            return nums[0]
        return self.rotatedbs(nums,len(nums),0,len(nums)-1)

    def rotatedbs(self,arr,n,lo,hi):
        while(lo<=hi):
            # this case is added if we get sorted on both sides of mid
            if arr[lo]<=arr[hi]:
                return arr[lo]
            
            mid=lo+(hi-lo)//2
            nxt=(mid+1)%n
            prev=(mid+n-1)%n
            if arr[mid]<=arr[nxt] and arr[mid]<=arr[prev]:
                return arr[mid]
            if arr[lo]<=arr[mid]:
                lo=mid+1 
            elif arr[mid]<=arr[hi]:
                hi=mid-1 
        return -1
    
    