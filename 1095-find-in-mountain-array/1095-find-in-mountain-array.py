# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:
class Solution:
    # 1->Find peak element
    # 2->Binary search in asc arr
    # 3-> if not found bs in desc arr
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        peak=self.peakIndexInMountainArray(mountain_arr)
        firstTry=self.orderAgnoBinarySearch(mountain_arr,target,0,peak)
        print(peak,firstTry)
        if firstTry!=-1:
            return firstTry
        return self.orderAgnoBinarySearch(mountain_arr,target,peak+1,mountain_arr.length()-1)
    
    def peakIndexInMountainArray(self, a: List[int]) -> int:
        # Binary Search
        l=0
        h=a.length()-1
        while(l<h):
            mid=l+(h-l)//2
            if a.get(mid)>a.get(mid+1):
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
            
        
    def orderAgnoBinarySearch(self,nums,target,start,end):
      # check for ascending order
      # isAsc=nums[start]<nums[end]
      # or
        
        if nums.get(start)<nums.get(end):
            isAsc=True
        else:
            isAsc=False 

        while(start<=end):
            mid = start+(end-start)//2
            if nums.get(mid)==target:
                return mid 
            
            if isAsc:
                if target<nums.get(mid):
                    end=mid-1
                elif target>nums.get(mid):
                    start= mid+1
            else:
                if target>nums.get(mid):
                    end=mid-1
                elif target<nums.get(mid):
                    start= mid+1
        return -1