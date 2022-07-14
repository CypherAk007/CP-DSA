class Solution:
    # find the pivot-largest element
    # next find in the first half of arr if not second half
    
    def search(self, nums: List[int], target: int) -> int:
        pivot=self.findPivot(nums)
        # // if no pivot that means the array in not rotated
        if pivot==-1:
            # just do normal binary search
            return self.binarySearch(nums,target,0,len(nums)-1)
        # if pivot is found then we have 2 asc arrays
        # 3cases
        if nums[pivot]==target:
            return pivot
        if target>=nums[0]:
            return self.binarySearch(nums,target,0,pivot-1)
        return self.binarySearch(nums,target,pivot+1,len(nums)-1)
    
        
    def findPivot(self,arr):
        start=0
        end=len(arr)-1
        while(start<=end):
            mid=start+(end-start)//2
            # 4cases 
            if mid<end and arr[mid]>arr[mid+1]:
                return mid
            if mid>start and arr[mid]<arr[mid-1]:
                return mid
            if arr[mid]<=arr[start]:
                end=mid-1
            else:#start<mid
                start=mid+1
        return -1
    def binarySearch(self,nums,target,start,end):
        while(start<=end):
            mid = start+(end-start)//2

            if target<nums[mid]:
                end=mid-1
            elif target>nums[mid]:
                start= mid+1
            else:
            #find the ans
                return mid
        return -1